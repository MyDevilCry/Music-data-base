from typing import ClassVar

from django.contrib import admin

from artists.models import Artists, Genre, Release


@admin.register(Artists)
class ArtistsAdmin(admin.ModelAdmin):
    list_display=('name','slug','artists_type',)
    prepopulated_fields:ClassVar[dict[str,tuple[str, ...]]]={'slug':('name',)}


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display=('name',)

@admin.register(Release)
class ReleasesAdmin(admin.ModelAdmin):
    list_display=('name','release_type',)
