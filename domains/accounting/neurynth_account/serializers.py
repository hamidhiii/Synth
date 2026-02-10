from rest_framework import serializers
from .models import (
    AccountAccount, AccountJournal, AccountTax, 
    AccountMove, AccountMoveLine, AccountInvoice, 
    account_payment, AccountAccountType, AccountTaxGroup
)

class AccountAccountTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountAccountType
        fields = '__all__'

class AccountAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountAccount
        fields = '__all__'

class AccountJournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountJournal
        fields = '__all__'

class AccountTaxGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountTaxGroup
        fields = '__all__'

class AccountTaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountTax
        fields = '__all__'

class AccountMoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountMove
        fields = '__all__'

class AccountMoveLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountMoveLine
        fields = '__all__'

class AccountInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountInvoice
        fields = '__all__'

class AccountPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = account_payment
        fields = '__all__'
