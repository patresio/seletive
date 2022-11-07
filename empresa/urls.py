from django.urls import path
from . import views

urlpatterns = [
    path('novaEmpresa/', views.novaEmpresa, name='novaEmpresa'),
]
