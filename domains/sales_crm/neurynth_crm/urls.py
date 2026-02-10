from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LeadViewSet, TagViewSet, TeamViewSet

router = DefaultRouter()
router.register(r'leads', LeadViewSet)
router.register(r'tags', TagViewSet)
router.register(r'teams', TeamViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
