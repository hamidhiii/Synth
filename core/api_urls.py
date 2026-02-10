from django.urls import path, include

urlpatterns = [
    path('crm/', include('neurynth_crm.urls')),
    path('sale/', include('neurynth_sale.urls')),
    path('accounting/', include('neurynth_account.urls')),
    path('hr/', include('neurynth_hr.urls')),
    path('inventory/', include('neurynth_stock.urls')),
    path('manufacturing/', include('neurynth_mrp.urls')),
]
