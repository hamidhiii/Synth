from rest_framework import viewsets
from .models import SaleOrder, SaleOrderLine, AccountInvoice, SaleLayoutCategory
from .serializers import (
    SaleOrderSerializer, 
    SaleOrderLineSerializer, 
    AccountInvoiceSerializer, 
    SaleLayoutCategorySerializer
)

class SaleOrderViewSet(viewsets.ModelViewSet):
    queryset = SaleOrder.objects.all()
    serializer_class = SaleOrderSerializer

class SaleOrderLineViewSet(viewsets.ModelViewSet):
    queryset = SaleOrderLine.objects.all()
    serializer_class = SaleOrderLineSerializer

class AccountInvoiceViewSet(viewsets.ModelViewSet):
    queryset = AccountInvoice.objects.all()
    serializer_class = AccountInvoiceSerializer

class SaleLayoutCategoryViewSet(viewsets.ModelViewSet):
    queryset = SaleLayoutCategory.objects.all()
    serializer_class = SaleLayoutCategorySerializer
