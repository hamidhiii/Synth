from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    LocationViewSet, WarehouseViewSet, StockMoveViewSet, 
    StockMoveLineViewSet, PickingViewSet, StockQuantViewSet
)

router = DefaultRouter()
router.register(r'locations', LocationViewSet)
router.register(r'warehouses', WarehouseViewSet)
router.register(r'moves', StockMoveViewSet)
router.register(r'move-lines', StockMoveLineViewSet)
router.register(r'pickings', PickingViewSet)
router.register(r'quants', StockQuantViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
