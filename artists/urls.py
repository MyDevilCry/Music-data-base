from django.urls import path
from artists import views

app_name='artists'

urlpatterns = [
    path('',views.CatalogView.as_view(),name="index"),
    path('add_artists/',views.AddArtistView.as_view(),name="add_artists"),
    path('creation_genre/',views.CreateGenreView.as_view(),name='creation_genre')
]
