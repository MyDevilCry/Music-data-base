from django.views.generic import ListView, CreateView

from artists.models import  Genre

#Створили голову сторінку де будуть жанри музики
class CatalogView(ListView):
    template_name='artists/main.html'
    model=Genre
    context_object_name='genres'

class CreateGenreView(CreateView):
    template_name='artists/main.html'
    form_class=user





