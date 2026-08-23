from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from artists.forms import CreateGenreForm, AddArtistsForm
from artists.models import  Genre

User=get_user_model()


class CatalogView(ListView):
    model = Genre
    template_name='artists/genres.html'
    context_object_name='genres'
    extra_context={'title':'genres'}


class AddArtistView(LoginRequiredMixin,CreateView):
    template_name = 'artists/add_artist.html'
    form_class=AddArtistsForm
    login_url='users:login'
    success_url=reverse_lazy('artists:artists')
    extra_context={'title':'add an artist'}



class CreateGenreView(LoginRequiredMixin,CreateView):#Роблю створення жанрів
    template_name='artists/create_genre.html'
    form_class=CreateGenreForm
    login_url = 'users:login'
    success_url=reverse_lazy('artists:genres')
    extra_context = {'title':'Creation genre'}



