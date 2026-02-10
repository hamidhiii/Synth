from rest_framework import viewsets
from .models import (
    AccountAccount, AccountJournal, AccountTax, 
    AccountMove, AccountMoveLine, AccountInvoice, 
    account_payment, AccountAccountType, AccountTaxGroup
)
from .serializers import (
    AccountAccountSerializer, AccountJournalSerializer, AccountTaxSerializer,
    AccountMoveSerializer, AccountMoveLineSerializer, AccountInvoiceSerializer,
    AccountPaymentSerializer, AccountAccountTypeSerializer, AccountTaxGroupSerializer
)

class AccountAccountTypeViewSet(viewsets.ModelViewSet):
    queryset = AccountAccountType.objects.all()
    serializer_class = AccountAccountTypeSerializer

class AccountAccountViewSet(viewsets.ModelViewSet):
    queryset = AccountAccount.objects.all()
    serializer_class = AccountAccountSerializer

class AccountJournalViewSet(viewsets.ModelViewSet):
    queryset = AccountJournal.objects.all()
    serializer_class = AccountJournalSerializer

class AccountTaxGroupViewSet(viewsets.ModelViewSet):
    queryset = AccountTaxGroup.objects.all()
    serializer_class = AccountTaxGroupSerializer

class AccountTaxViewSet(viewsets.ModelViewSet):
    queryset = AccountTax.objects.all()
    serializer_class = AccountTaxSerializer

class AccountMoveViewSet(viewsets.ModelViewSet):
    queryset = AccountMove.objects.all()
    serializer_class = AccountMoveSerializer

class AccountMoveLineViewSet(viewsets.ModelViewSet):
    queryset = AccountMoveLine.objects.all()
    serializer_class = AccountMoveLineSerializer

class AccountInvoiceViewSet(viewsets.ModelViewSet):
    queryset = AccountInvoice.objects.all()
    serializer_class = AccountInvoiceSerializer

class AccountPaymentViewSet(viewsets.ModelViewSet):
    queryset = account_payment.objects.all()
    serializer_class = AccountPaymentSerializer
