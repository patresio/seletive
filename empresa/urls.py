from django.urls import path
from . import views

urlpatterns = [
    path('', views.empresas, name='empresas'),
    path('novaEmpresa/', views.novaEmpresa, name='novaEmpresa'),
    path('excluirEmpresa/<str:id>', views.excluirEmpresa, name='excluirEmpresa')
]
