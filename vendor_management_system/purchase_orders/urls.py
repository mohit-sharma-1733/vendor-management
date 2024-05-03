from django.urls import path
from .views import PurchaseOrderListCreateView, PurchaseOrderRetrieveUpdateDestroyView,AcknowledgePurchaseOrderView

urlpatterns = [
    path('api/purchase_orders/', PurchaseOrderListCreateView.as_view(), name='purchase-order-list-create'),
    path('api/purchase_orders/<int:pk>/', PurchaseOrderRetrieveUpdateDestroyView.as_view(), name='purchase-order-retrieve-update-destroy'),
    path('api/purchase_orders/<int:po_id>/acknowledge/', AcknowledgePurchaseOrderView.as_view(), name='acknowledge_purchase_order'),
]
