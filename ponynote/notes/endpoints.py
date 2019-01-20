from django.urls import include, path
from rest_framework import routers

from .api import NoteViewSet, RegistrationAPI, LoginAPI, UserAPI

router = routers.DefaultRouter()
router.register('notes', NoteViewSet, 'notes')

urlpatterns = [
    path("", include(router.urls)),
    path("auth/register/", RegistrationAPI.as_view()),
    path("auth/login/", LoginAPI.as_view()),
    path("auth/user/", UserAPI.as_view()),
]