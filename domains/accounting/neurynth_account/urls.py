from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AccountAccountViewSet, AccountJournalViewSet, AccountTaxViewSet,
    AccountMoveViewSet, AccountMoveLineViewSet, AccountInvoiceViewSet,
    AccountPaymentViewSet, AccountAccountTypeViewSet, AccountTaxGroupViewSet
)

router = DefaultRouter()
router.register(r'account-types', AccountAccountTypeViewSet)
router.register(r'accounts', AccountAccountViewSet)
router.register(r'journals', AccountJournalViewSet)
router.register(r'tax-groups', AccountTaxGroupViewSet)
router.register(r'taxes', AccountTaxViewSet)
router.register(r'moves', AccountMoveViewSet)
router.register(r'move-lines', AccountMoveLineViewSet)
router.register(r'invoices', AccountInvoiceViewSet)
router.register(r'payments', AccountPaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
