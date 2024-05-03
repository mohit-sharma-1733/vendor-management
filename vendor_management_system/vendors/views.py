from rest_framework import generics
from .models import Vendor
from .serializers import VendorSerializer
from django.http import JsonResponse
from django.db.models import Avg, Count, F
from django.views import View
from datetime import timedelta
from purchase_orders.models import PurchaseOrder
class VendorListCreateView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorPerformanceView(View):
    def get(self, request, vendor_id):
        try:
            vendor = Vendor.objects.get(pk=vendor_id)
        except Vendor.DoesNotExist:
            return JsonResponse({'error': 'Vendor not found'}, status=404)

        total_orders = PurchaseOrder.objects.filter(vendor=vendor).count()
        if total_orders == 0:
            return JsonResponse({'error': 'No purchase orders found for this vendor'}, status=404)

        on_time_delivery_rate = PurchaseOrder.objects.filter(vendor=vendor, status='completed', delivery_date__lte=F('acknowledgment_date')).count() / total_orders * 100
        quality_rating_avg = PurchaseOrder.objects.filter(vendor=vendor, quality_rating__isnull=False).aggregate(avg_quality_rating=Avg('quality_rating'))['avg_quality_rating'] or 0
        average_response_time = PurchaseOrder.objects.filter(vendor=vendor, acknowledgment_date__isnull=False).aggregate(avg_response_time=Avg(F('acknowledgment_date') - F('issue_date')))['avg_response_time'] or timedelta(seconds=0)
        fulfillment_rate = PurchaseOrder.objects.filter(vendor=vendor, status='completed').count() / total_orders * 100

        performance_data = {
            'on_time_delivery_rate': round(on_time_delivery_rate, 2),
            'quality_rating_avg': round(quality_rating_avg, 2),
            'average_response_time': round(average_response_time.total_seconds() / 3600, 2),  # Convert to hours
            'fulfillment_rate': round(fulfillment_rate, 2)
        }

        return JsonResponse(performance_data)