from django.urls import path
from . import views

urlpatterns = [
    path('', views.labReport, name = 'lab'),
]
