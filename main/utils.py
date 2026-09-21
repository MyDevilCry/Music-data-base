from django.contrib.postgres.search import (
    SearchHeadline,
    SearchQuery,
    SearchRank,
    SearchVector,
)

from artists.models import Artists


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Artists.objects.filter(id=int(query))
    vector = SearchVector("name", "description","genre",)
    query = SearchQuery(query)

    result = (
        Artists.objects.annotate(rank=SearchRank(vector, query))
        .filter(rank__gt=0)
        .order_by("-rank")
    )

    result = result.annotate(
        headline=SearchHeadline(
            "name",
            query,
            start_sel='<span style="background-color:yellow;">',
            stop_sel="</span>",
        ),
        bodyline=SearchHeadline(
            "description",
            query,
            start_sel='<span style="background-color:yellow;">',
            stop_sel="</span>",
        ),
        genreline=SearchHeadline(
            "genre",
            query,
            start_sel='<span style="background-color:yellow;">',
            stop_sel="</span>",
        )
    )
    return result
