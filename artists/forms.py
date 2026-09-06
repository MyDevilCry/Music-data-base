from django import forms

from artists.models import Artists, Genre


class GenreCreateForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ("name",)


class AddArtistsForm(forms.ModelForm):
    class Meta:
        model = Artists
        fields = ("name", "genre")
