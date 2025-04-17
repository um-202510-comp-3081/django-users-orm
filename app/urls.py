from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path("users/", views.user_list, name="user_list"),
    path("users/<int:id>", views.user_details, name="user_details"),
]
