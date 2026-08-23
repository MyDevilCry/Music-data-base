from django import forms
from artists.models import Genre, Artists


class CreateGenreForm(forms.ModelForm):
    class Meta:
        model=Genre
        fields=['name']

class AddArtistsForm(forms.ModelForm):
    class Meta:
        model=Artists
        fields=['name','genre']



