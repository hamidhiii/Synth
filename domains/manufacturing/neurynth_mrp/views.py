from rest_framework import viewsets
from .models import MrpBom, MrpProduction, MrpWorkcenter, MrpWorkorder
from .serializers import MrpBomSerializer, MrpProductionSerializer, MrpWorkcenterSerializer, MrpWorkorderSerializer

class MrpBomViewSet(viewsets.ModelViewSet):
    queryset = MrpBom.objects.all()
    serializer_class = MrpBomSerializer

class MrpProductionViewSet(viewsets.ModelViewSet):
    queryset = MrpProduction.objects.all()
    serializer_class = MrpProductionSerializer

class MrpWorkcenterViewSet(viewsets.ModelViewSet):
    queryset = MrpWorkcenter.objects.all()
    serializer_class = MrpWorkcenterSerializer

class MrpWorkorderViewSet(viewsets.ModelViewSet):
    queryset = MrpWorkorder.objects.all()
    serializer_class = MrpWorkorderSerializer
