from django.urls import path
from . import views

urlpatterns = [
    path('novaVaga/', views.novaVaga, name="novaVaga"),
]