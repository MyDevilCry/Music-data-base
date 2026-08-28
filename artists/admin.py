from django.contrib import admin

from artists.models import Artists, Genre, Release


# Register your models here.

@admin.register(Artists)
class ArtistsAdmin(admin.ModelAdmin):
    list_display=('name','artists_type',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display=('name',)

@admin.register(Release)
class ReleasesAdmin(admin.ModelAdmin):
    list_display=('name','release_type',)
