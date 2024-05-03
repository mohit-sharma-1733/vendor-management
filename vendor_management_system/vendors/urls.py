from django.urls import path
from .views import VendorListCreateView, VendorRetrieveUpdateDestroyView, VendorPerformanceView

urlpatterns = [
    path('api/vendors/', VendorListCreateView.as_view(), name='vendor-list-create'),
    path('api/vendors/<int:pk>/', VendorRetrieveUpdateDestroyView.as_view(), name='vendor-retrieve-update-destroy'),
    path('api/vendors/<int:vendor_id>/performance/', VendorPerformanceView.as_view(), name='get_vendor_performance'),
]
