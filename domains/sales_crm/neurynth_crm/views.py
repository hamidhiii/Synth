from rest_framework import viewsets
from .models import Lead, Tag, Team
from .serializers import LeadSerializer, TagSerializer, TeamSerializer

class LeadViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows leads/opportunities to be viewed or edited.
    """
    queryset = Lead.objects.all().order_by('-create_date')
    serializer_class = LeadSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
