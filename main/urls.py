from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("code.net/", views.code, name="code"),
    path("darkwilderness/", views.dark_wilderness, name="darkwilderness"),
]