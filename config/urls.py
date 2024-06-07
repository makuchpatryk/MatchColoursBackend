from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from MatchColourBackend.config import settings

urlpatterns = [
   path("admin/", admin.site.urls),
   path("api/", include("app.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)