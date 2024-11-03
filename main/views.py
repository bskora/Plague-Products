from django.shortcuts import render
from django.views.generic import ListView
from main.models import Post

# Create your views here.
class NewsView(ListView):
    model = Post
    template_name = "updates.html"

    def get_queryset(self, *args, **kwargs):
        qs = super(NewsView, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("-id")
        return qs

def home(response):
    return render(response, "home.html", {})

def updates(response):
    return render(response, "updates.html", {})

def code(response):
    return render(response, "codenet.html", {})

def enduring_wilderness(response):
    return render(response, "enduringwilderness.html", {})

def private_policy(response):
    return render(response, "privatepolicy.html", {})

def terms_of_service(response):
    return render(response, "termsofservice.html", {})