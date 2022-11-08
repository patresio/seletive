from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants
from .models import Tecnologia, Empresa

# Create your views here.

def novaEmpresa(request):
    if request.method == "GET":
        techs = Tecnologia.objects.all()
        nichosMercado = Empresa.choices_nicho_mercado
        return render(request, 'novaEmpresa.html', {'techs': techs, 'nichosMercado': nichosMercado})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cidade = request.POST.get('cidade')
        endereco = request.POST.get('endereco')
        nicho = request.POST.get('nicho')
        caracteristicas = request.POST.get('caracteristicas')
        tecnologias = request.POST.getlist('tecnologias')
        logo = request.FILES.get('logo')

        if (len(nome.strip()) == 0 or len(email.strip()) == 0 or len(cidade.strip()) == 0 or len(endereco.strip()) == 0 or len(nicho.strip()) == 0 or len(caracteristicas.strip()) == 0 or (not logo)): 
            messages.add_message(request, messages.ERROR, 'Preencha todos os campos')
            return redirect('/empresas/novaEmpresa')

        if logo.size > 100_000_000:
            messages.add_message(request, constants.ERROR, 'A logo da empresa deve ter menos de 10MB')
            return redirect('/empresas/novaEmpresa')

        if nicho not in [i[0] for i in Empresa.choices_nicho_mercado]:
            messages.add_message(request, constants.ERROR, 'Nicho de mercado inválido')
            return redirect('/empresas/novaEmpresa')

        empresa = Empresa(
            logo=logo,
            nome=nome,
            cidade=cidade,
            endereco=endereco,
            nicho_mercado=nicho,
            caracteristica_empresa=caracteristicas,
        )
        empresa.save()
        empresa.tecnologias.add(*tecnologias)
        empresa.save()

        messages.add_message(request, constants.SUCCESS, 'Empresa cadastrada com sucesso')
        return redirect('/empresas/novaEmpresa')


def empresas(request):
    empresas = Empresa.objects.all()
    tecnologias = Tecnologia.objects.all()
    return render(request, 'empresas.html', {'empresas': empresas, 'tecnologias': tecnologias})

def excluirEmpresa(request, id):
    empresa = Empresa.objects.filter(id=id)
    empresa.delete()
    messages.add_message(request, constants.SUCCESS, f'Empresa {empresa.nome} excluida com sucesso')
    return redirect('empresas/')