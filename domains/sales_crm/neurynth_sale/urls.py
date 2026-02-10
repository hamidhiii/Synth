from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SaleOrderViewSet, 
    SaleOrderLineViewSet, 
    AccountInvoiceViewSet, 
    SaleLayoutCategoryViewSet
)

router = DefaultRouter()
router.register(r'orders', SaleOrderViewSet)
router.register(r'order-lines', SaleOrderLineViewSet)
router.register(r'invoices', AccountInvoiceViewSet)
router.register(r'layout-categories', SaleLayoutCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
