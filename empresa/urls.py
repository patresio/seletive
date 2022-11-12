from django.urls import path
from . import views

urlpatterns = [
    path('', views.empresas, name='empresas'),
    path('novaEmpresa/', views.novaEmpresa, name='novaEmpresa'),
    path('excluirEmpresa/<str:pk>', views.excluirEmpresa, name='excluirEmpresa'),
    path('empresa/<str:pk>', views.empresa, name='empresa'),
]
