from rest_framework import generics
from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer
from django.http import JsonResponse
from django.utils import timezone
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt,csrf_protect
class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

#@csrf_exempt
class AcknowledgePurchaseOrderView(APIView):
    
    def post(self, request, po_id):
        purchase_order = self.get_purchase_order(po_id)
        if not purchase_order:
            return JsonResponse({'error': 'Purchase order not found'}, status=404)

        # Update acknowledgment_date to current timestamp
        purchase_order.acknowledgment_date = timezone.now()
        purchase_order.save()

        # Recalculate average_response_time for the vendor
        vendor = purchase_order.vendor
        vendor.calculate_average_response_time()

        return JsonResponse({'message': 'Purchase order acknowledged successfully'}, status=200)

    def get_purchase_order(self, po_id):
        try:
            return PurchaseOrder.objects.get(pk=po_id)
        except PurchaseOrder.DoesNotExist:
            return None

    def get(self, request, po_id):
        return JsonResponse({'error': 'Method not allowed'}, status=405)