from django.urls import path
from . import views

urlpatterns = [
    path('', views.empresas, name='empresas'),
    path('novaEmpresa/', views.novaEmpresa, name='novaEmpresa'),
    path('excluirEmpresa/<int:id>', views.excluirEmpresa, name='excluirEmpresa'),
    path('empresa/<int:id>', views.empresa, name='empresa'),
]
