from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MrpBomViewSet, MrpProductionViewSet, MrpWorkcenterViewSet, MrpWorkorderViewSet

router = DefaultRouter()
router.register(r'boms', MrpBomViewSet)
router.register(r'productions', MrpProductionViewSet)
router.register(r'workcenters', MrpWorkcenterViewSet)
router.register(r'workorders', MrpWorkorderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
