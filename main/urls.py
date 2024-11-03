from django.urls import path
from .views import NewsView

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("updates/", NewsView.as_view(), name="update"),
    path("code.net/", views.code, name="code"),
    path("enduringwilderness/", views.enduring_wilderness, name="enduringwilderness"),
    path("privatepolicy/", views.private_policy, name="privatepolicy"),
    path("termsofservice/", views.terms_of_service, name="termsofservice"),
]