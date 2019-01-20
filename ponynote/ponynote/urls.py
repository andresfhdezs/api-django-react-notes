from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from notes import endpoints

urlpatterns = [
    path("api/", include(endpoints)),
    path('admin/', admin.site.urls),
    path('api/auth/', include('knox.urls')),
    path("", TemplateView.as_view(template_name="index.html")),
]
