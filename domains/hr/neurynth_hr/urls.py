from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, DepartmentViewSet, JobViewSet, EmployeeCategoryViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'jobs', JobViewSet)
router.register(r'categories', EmployeeCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
