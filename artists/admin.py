from typing import ClassVar

from django.contrib import admin

from artists.models import Artists, Genre, Release


@admin.register(Artists)
class ArtistsAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
        "artists_type",
    )
    prepopulated_fields: ClassVar[dict[str, tuple[str, ...]]] = {"slug": ("name",)}
    search_fields = ("name",)
    autocomplete_fields = ("genre",)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Release)
class ReleasesAdmin(admin.ModelAdmin):
    list_display = (
        "release_name",
        "release_type",
    )
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("release_name",)}
    autocomplete_fields = ("genres", "artists")

