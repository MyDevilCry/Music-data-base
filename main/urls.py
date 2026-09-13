from django.urls import path

from main import views

app_name = "main"

urlpatterns = [
    path("", views.MainView.as_view(), name="main"),
    path("search_result/", views.SearchResultsView.as_view(), name="search_result"),
]
