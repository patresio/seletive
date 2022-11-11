from django.urls import path
from . import views

urlpatterns = [
    path('novaVaga/', views.novaVaga, name="novaVaga"),
    path('vaga/<str:pk>', views.vaga, name="vaga"),
    path('nova_tarefa/<str:pk_vaga>', views.novaTarefa, name="nova_tarefa"),
    path('realizar_tarefa/<str:pk>', views.realizarTarefa, name='realizar_tarefa'),
    path('envia_email/<str:pk_vaga>', views.enviaEmail, name='envia_email')
]