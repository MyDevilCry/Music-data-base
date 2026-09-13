from django.urls import path

from artists import views

app_name = "artists"

urlpatterns = [
    path("", views.ListView.as_view(), name="main"),
    path("releases", views.ReleasesView.as_view(), name="releases"),
    path("release/<slug:slug>/",views.ReleasesDetailView.as_view(), name="releases_detail"),
    path("<slug:slug>/", views.ArtistsDetailView.as_view(), name="artists_detail"),
]
