from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MedicineViewSet

# Initialize the router
router = DefaultRouter()
router.register(r'medicines', MedicineViewSet, basename='medicine')

# Register routes with Django
urlpatterns = [
    path('', include(router.urls)),  # Include the router's generated URLs
]
