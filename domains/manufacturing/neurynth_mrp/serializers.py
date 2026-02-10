from rest_framework import serializers
from .models import MrpBom, MrpProduction, MrpWorkcenter, MrpWorkorder

class MrpBomSerializer(serializers.ModelSerializer):
    class Meta:
        model = MrpBom
        fields = '__all__'

class MrpProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MrpProduction
        fields = '__all__'

class MrpWorkcenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MrpWorkcenter
        fields = '__all__'

class MrpWorkorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MrpWorkorder
        fields = '__all__'
