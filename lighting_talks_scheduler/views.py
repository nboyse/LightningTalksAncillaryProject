from django.shortcuts import render


def homepage(request):
    return render(request, "homepage.html")

def name(request):
    return render(request, "name.html")
