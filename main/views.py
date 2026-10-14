from django.db.models import Q
from django.views.generic import TemplateView

from artists.models import Artists, Genre, Release


class MainView(TemplateView):
    template_name = "main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["artists"] = Artists.objects.with_genres().order_by("?")[:10]
        context["genres"] = Genre.objects.order_by("?")[:16]
        context["random_release"] = (
            Release.objects.published_with_relations()
            .filter(
                release_type__in=[
                    "Album",
                    "EP",
                ]
            )
            .order_by("?")[:10]
        )

        return context


class SearchResultsView(TemplateView):
    template_name = "search_result.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get("q", "")

        if query:
            context["found_artists"] = Artists.objects.with_genres().filter(
                Q(name__icontains=query) | Q(genre__name__icontains=query)
            )
            context["found_genres"] = Genre.objects.filter(Q(name__icontains=query))
            context["found_releases"] = Release.objects.published_with_relations.filter(
                Q(release_name__icontains=query) | Q(artists__name__icontains=query)
            )
            context["query"] = query
        return context
