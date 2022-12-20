from django.urls import path
from .views import NewsView

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("news/", NewsView.as_view(), name="news"),
    path("code.net/", views.code, name="code"),
    path("darkwilderness/", views.dark_wilderness, name="darkwilderness"),
]