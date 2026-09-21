from django.urls import path

from artists import views

app_name = "artists"

urlpatterns = [
    path("", views.ListView.as_view(), name="main"),
    path("releases", views.ReleasesView.as_view(), name="releases"),
    path("genre/<slug:slug>/",views.GenreDetailView.as_view(), name= "genre_detail"),
    path("release/<slug:slug>/",views.ReleasesDetailView.as_view(), name="releases_detail"),
    path("<slug:slug>/", views.ArtistsDetailView.as_view(), name="artists_detail"),
    path("artist/<slug:slug>/favorite/", views.toggle_favorite_artists, name='toggle_favorite_artist'),
    path("release/<slug:slug>/favorite/", views.toggle_favorite_releases, name='toggle_favorite_releases')
]
