from django.urls import path
from artists import views

app_name='artists'

urlpatterns = [
    path('',views.ListView.as_view(),name="main"),
    path('artists',views.BandOrArtistView.as_view(),name="artists"),
    path('releases',views.ReleasesView.as_view(),name="releases"),
    path('add_artists/',views.AddArtistView.as_view(),name="add_artists"),
    path('creation_genre/',views.CreateGenreView.as_view(),name="creation_genre"),
    path('<slug:slug>/',views.ArtistsDetailView.as_view(),name='artists_detail'),
]
