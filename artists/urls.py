from django.urls import include, path
from rest_framework.routers import DefaultRouter

from artists import views
from artists.views import ArtistViewSet, ReleaseViewSet

app_name = "artists"

router = DefaultRouter()
router.register("artists", ArtistViewSet, basename="artist")
router.register("releases", ReleaseViewSet, basename="release")

urlpatterns = [
    path("", views.ListView.as_view(), name="main"),
    path("api/", include(router.urls)),
    path("releases", views.ReleasesView.as_view(), name="releases"),
    path("genre/<slug:slug>/", views.GenreDetailView.as_view(), name="genre_detail"),
    path(
        "release/<slug:slug>/",
        views.ReleasesDetailView.as_view(),
        name="releases_detail",
    ),
    path("<slug:slug>/", views.ArtistsDetailView.as_view(), name="artists_detail"),
    path(
        "artist/<slug:slug>/favorite/",
        views.toggle_favorite_artists,
        name="toggle_favorite_artist",
    ),
    path(
        "release/<slug:slug>/favorite/",
        views.toggle_favorite_releases,
        name="toggle_favorite_releases",
    ),
]
