from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from config import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls", namespace="main")),
    path("user/", include("users.urls", namespace="users")),
    path("artist/", include("artists.urls", namespace="artists")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
