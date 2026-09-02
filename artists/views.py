from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from artists.forms import CreateGenreForm, AddArtistsForm
from artists.models import Artists, Release

User=get_user_model()


class BandOrArtistView(ListView):
    model=Artists
    template_name='artists/artists.html'
    context_object_name='Artists'
    extra_context={'title':'artists'}


@login_required
def add_artists(request):
    if request.method=='POST':
        form=AddArtistsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('artists/artists.html')

    else:
        form=AddArtistsForm()
    return render(request, 'artists/add_artists.html',{'form':form})


class ArtistsDetailView(DetailView):
    model= Artists
    template_name='artists_detail.html'
    context_object_name = 'artist'
    extra_context={'title':'artist',}


class AddArtistView(LoginRequiredMixin,CreateView):
    template_name = 'artists/add_artist.html'
    form_class=AddArtistsForm
    login_url='users:login'
    success_url=reverse_lazy('artists:artists')
    extra_context={'title':'artist'}



class CreateGenreView(LoginRequiredMixin,CreateView):#Роблю створення жанрів
    template_name='artists/create_genre.html'
    form_class=CreateGenreForm
    login_url = 'users:login'
    success_url=reverse_lazy('artists:genres')
    extra_context = {'title':'genre'}


class ReleasesView(ListView):
    model=Release
    template_name='artists/releases.html'
    context_object_name = 'Releases'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['random_release'] = Release.objects.all()
        return context

class ReleasesDetailView(DetailView):
    model=Release
    template_name = 'artists/release_detail.html'
    context_object_name = 'releases'
    extra_context = {'title':'release'}







