from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from backend import settings
from backend.views import get_points

urlpatterns = [
    path('/', TemplateView.as_view(template_name="index.html")),
    path('get_points/', get_points),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL,
           document_root=settings.STATIC_ROOT)
