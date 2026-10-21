from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, ListView
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from artists.models import Artists, Genre, Release
from artists.serializers import (
    ArtistDetailSerializer,
    ArtistSerializer,
    ReleaseDetailSerializer,
    ReleaseSerializer,
)
from main.services import (
    fetch_and_save_album_data,
    fetch_and_save_artist_data,
    get_wikipedia_album_summary,
)

User = get_user_model()


class ArtistsDetailView(DetailView):
    model = Artists
    template_name = "artists_detail.html"
    context_object_name = "artist"




    def get_queryset(self):
        return super().get_queryset()

    def get_object(self, queryset=None):
        artists = super().get_object(queryset)

        if not artists.is_fetched:
            fetch_and_save_artist_data(artists.id)
            artists.refresh_from_db()

        return artists


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["release_artist_detail"] = (
            Release.objects.published_with_relations().filter(artists=self.object)
        )
        return context




@login_required
def toggle_favorite_artists(request, slug):
    artist = get_object_or_404(Artists, slug=slug)
    if artist in request.user.favorite_artists.all():
        request.user.favorite_artists.remove(artist)
    else:
        request.user.favorite_artists.add(artist)

    return redirect("artists:artists_detail", slug=slug)


class GenreDetailView(ListView):
    model = Artists
    template_name = "genres.html"
    context_object_name = "artists"

    def get_queryset(self):
        genre_slug = self.kwargs["slug"]
        return Artists.objects.with_genres().filter(genre__slug=genre_slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["genre"] = Genre.objects.get(slug=self.kwargs["slug"])
        return context


class ReleasesView(ListView):
    model = Release
    template_name = "artists/releases.html"
    context_object_name = "releases"

    def get_queryset(self):
        return Release.objects.published_with_relations()


class ReleasesDetailView(DetailView):
    model = Release
    template_name = "releases_detail.html"
    context_object_name = "release"



    def get_queryset(self):
        return Release.objects.published_with_relations()

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if not obj.tracks.exists():
            fetch_and_save_album_data(obj.id)
            obj.refresh_from_db()

        if not obj.release_description:
            artist_name = obj.artists.name if obj.artists else ""
            wiki_summary = get_wikipedia_album_summary(obj.release_name, artist_name)

            if wiki_summary:
                obj.release_description = wiki_summary
                obj.save()

        return obj


@login_required

def toggle_favorite_releases(request, slug):
    release = get_object_or_404(Release, slug=slug)
    if release in request.user.favorite_releases.all():
        request.user.favorite_releases.remove(release)
    else:
        request.user.favorite_releases.add(release)

    return redirect("artists:releases_detail", slug=slug)

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artists.objects.prefetch_related("genre").all()
    filter_backends = [SearchFilter]
    search_fields = ("name", "slug", "year_formed", "genre__name")
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ArtistDetailSerializer
        return ArtistSerializer


class ReleaseViewSet(viewsets.ModelViewSet):
    queryset = Release.objects.prefetch_related("genres", "artists").all()
    filter_backends = [SearchFilter]
    search_fields = ("name", "slug", "year_formed", "release__name")
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ReleaseDetailSerializer
        return ReleaseSerializer
