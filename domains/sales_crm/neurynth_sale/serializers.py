from rest_framework import serializers
from .models import SaleOrder, SaleOrderLine, AccountInvoice, SaleLayoutCategory

class SaleOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleOrder
        fields = '__all__'

class SaleOrderLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleOrderLine
        fields = '__all__'

class AccountInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountInvoice
        fields = '__all__'

class SaleLayoutCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleLayoutCategory
        fields = '__all__'
