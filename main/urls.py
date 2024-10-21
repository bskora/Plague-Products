from django.urls import path
from .views import NewsView

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("updates/", NewsView.as_view(), name="news"),
    path("code.net/", views.code, name="code"),
    path("enduringwilderness/", views.enduring_wilderness, name="enduringwilderness"),
]