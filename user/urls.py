from django.urls import path, include
from rest_framework import routers
from .views import LipiAPIViewSet

default_router = routers.DefaultRouter(trailing_slash=False)

default_router.register('users', LipiAPIViewSet, basename='user')

urlpatterns = [
    path('', include(default_router.urls))
]