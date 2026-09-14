from django.contrib.auth import get_user_model
from django.views.generic import DetailView, ListView

from artists.models import Artists, Release
from main.services import fetch_and_save_album_data, get_wikipedia_album_summary

User = get_user_model()


class ArtistsDetailView(DetailView):
    model = Artists
    template_name = "artists_detail.html"
    context_object_name = "artist"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        artists = self.get_object()
        context["release_artist_detail"] = Release.objects.filter(
            artists=artists
        ).order_by("release_date")
        return context


class ReleasesView(ListView):
    model = Release
    template_name = "artists/releases.html"
    context_object_name = "Releases"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["random_release"] = Release.objects.all()
        return context


class ReleasesDetailView(DetailView):
    model = Release
    template_name = "releases_detail.html"
    context_object_name = "release"

    def get_object(self, queryset = None):
        obj = super().get_object(queryset)

        if not obj.tracks.exists():
            fetch_and_save_album_data(obj.id)
            obj.refresh_from_db()

        if not obj.release_description:
            artist_name = obj.artists.name if hasattr(obj, 'artists') and obj.artists else ""
            wiki_summary = get_wikipedia_album_summary(obj.release_name,artist_name)

            if wiki_summary:
                obj.release_description = wiki_summary
                obj.save()

        return obj

