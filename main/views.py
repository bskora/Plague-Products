from django.shortcuts import render

# Create your views here.
def home(response):
    return render(response, "home.html", {})

def code(response):
    return render(response, "codenet.html", {})

def dark_wilderness(response):
    return render(response, "darkwilderness.html", {})