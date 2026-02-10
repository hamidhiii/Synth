from rest_framework import viewsets
from .models import Location, Warehouse, StockMove, StockMoveLine, Picking, StockQuant
from .serializers import (
    LocationSerializer, WarehouseSerializer, StockMoveSerializer, 
    StockMoveLineSerializer, PickingSerializer, StockQuantSerializer
)

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

class StockMoveViewSet(viewsets.ModelViewSet):
    queryset = StockMove.objects.all()
    serializer_class = StockMoveSerializer

class StockMoveLineViewSet(viewsets.ModelViewSet):
    queryset = StockMoveLine.objects.all()
    serializer_class = StockMoveLineSerializer

class PickingViewSet(viewsets.ModelViewSet):
    queryset = Picking.objects.all()
    serializer_class = PickingSerializer

class StockQuantViewSet(viewsets.ModelViewSet):
    queryset = StockQuant.objects.all()
    serializer_class = StockQuantSerializer
