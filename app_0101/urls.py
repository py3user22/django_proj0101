from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('notes', views.notes),
    path('homepage', views.home),
    path('0101_homepage.html', views.home),
    path('0101_django_notes.html', views.notes),
    path('0103_django_serializations.html', views.notes2),

]