from django.urls import path
from main import views


app_name='main'

urlpatterns = [

    path('',views.MainView.as_view(),name='main'),

]