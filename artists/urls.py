from django.contrib import admin
from django.urls import path

app_name='artists'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.artists_list,name='artists_list'),
]
