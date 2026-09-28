from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from config import settings




urlpatterns = [
    path("admin/", admin.site.urls),
    path("artist/", include("artists.urls", namespace="artists")),
    path("", include("main.urls", namespace="main")),
    path("user/", include("users.urls", namespace="users")),
    path('api/token/', TokenObtainPairView.as_view(), name='token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
