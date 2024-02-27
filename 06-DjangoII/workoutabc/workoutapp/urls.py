from django.urls import path, include
from rest_framework import routers
from workoutapp.views import ClientViewSet


router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
