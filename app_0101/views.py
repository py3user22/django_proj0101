from django.shortcuts import render


def home(request):
    return render(request, '0101_homepage.html', {})

def notes(request):
    return render(request, '0101_django_notes.html', {})


