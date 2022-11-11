from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from empresa.models import Vagas
from django.contrib import messages
from django.contrib.messages import constants
from .models import Tarefa
# Create your views here.

def novaVaga(request):
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        email = request.POST.get('email')
        tecnologias_domina = request.POST.getlist('tecnologias_domina')
        tecnologias_nao_domina = request.POST.getlist('tecnologias_nao_domina')
        experiencia = request.POST.get('experiencia')
        data_final = request.POST.get('data_final')
        empresa = request.POST.get('empresa')
        status = request.POST.get('status')

        vaga = Vagas(
            titulo=titulo,
            email=email,
            nivel_experiencia=experiencia,
            data_final=data_final,
            empresa_id=empresa,
            status=status
        )

        vaga.save()
        
        vaga.tecnologias_estudar.add(*tecnologias_nao_domina)
        vaga.tecnologias_dominadas.add(*tecnologias_domina)

        vaga.save()
        messages.add_message(request, constants.SUCCESS, 'Vaga criada com sucesso.')
        return redirect(f'/empresa/{empresa}')

    elif request.method == "GET":
        raise Http404


def vaga(request, pk):
    vaga = get_object_or_404(Vagas, id=pk)
    tarefas = Tarefa.objects.filter(vaga=vaga).filter(realizada=False)

    context = {
        'vaga': vaga,
        'tarefas': tarefas,
    }
    return render(request, 'vaga.html', context)


def novaTarefa(request, pk_vaga):
    titulo = request.POST.get('titulo')
    prioridade = request.POST.get('prioridade')
    data = request.POST.get('data')

    #TODO: Inserir o esquema de verificação

    try:
        tarefa = Tarefa(
                vaga_id = pk_vaga,
                titulo = titulo,
                prioridade = prioridade,
                data = data
        )

        tarefa.save()

        messages.add_message(request, messages.SUCCESS, 'Tarefa criada com sucesso')
        return redirect(f'/vagas/vaga/{pk_vaga}')
    except:
        messages.add_message(request, messages.ERROR, 'Erro no sistema')
        return redirect(f'/vagas/vaga/{pk_vaga}')

def realizarTarefa(request, pk):
    tarefa_list = Tarefa.objects.filter(id=pk).filter(realizada=False)

    if not tarefa_list.exists():
        messages.add_message(request, messages.ERROR, 'Realize apenas uma tarefa válida')
        return redirect('/')

    tarefa = tarefa_list.first()
    tarefa.realizada = True
    tarefa.save()

    messages.add_message(request, messages.SUCCESS, 'Tarefa realizada com sucesso')
    return redirect(f'/vagas/vaga/{tarefa.vaga_id}')