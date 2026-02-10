from rest_framework import serializers
from .models import Location, Warehouse, StockMove, StockMoveLine, Picking, StockQuant

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'

class StockMoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockMove
        fields = '__all__'

class StockMoveLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockMoveLine
        fields = '__all__'

class PickingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picking
        fields = '__all__'

class StockQuantSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockQuant
        fields = '__all__'
