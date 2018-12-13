from django.urls import include, path
from rest_framework import routers

from .api import NoteViewSet

router = routers.DefaultRouter()
router.register('notes', NoteViewSet)

urlpatterns = [
    path("", include(router.urls)),
]