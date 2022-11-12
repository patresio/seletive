from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants
from .models import Tecnologia, Empresa, Vagas

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
            return redirect('novaEmpresa')

        if logo.size > 100_000_000:
            messages.add_message(request, constants.ERROR, 'A logo da empresa deve ter menos de 10MB')
            return redirect('novaEmpresa')

        if nicho not in [i[0] for i in Empresa.choices_nicho_mercado]:
            messages.add_message(request, constants.ERROR, 'Nicho de mercado inválido')
            return redirect('novaEmpresa')

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
        return redirect('novaEmpresa')


def empresas(request):
    tecnologias_filtrar = request.GET.get('tecnologias')
    nome_filtrar = request.GET.get('nome')
    empresas = Empresa.objects.all()
    tecnologias = Tecnologia.objects.all()

    if tecnologias_filtrar:
        empresas = empresas.filter(tecnologias=tecnologias_filtrar)
    
    if nome_filtrar:
        empresas = empresas.filter(nome__icontains=nome_filtrar)
    
    return render(request, 'empresas.html', {'empresas': empresas, 'tecnologias': tecnologias})

def excluirEmpresa(request, pk):
    empresa = Empresa.objects.filter(id=pk)
    if not empresa.delete():
        messages.add_message(request, messages.ERROR, 'Não foi possível excluir empresa')
        return redirect('empresas')
    elif empresa.delete():
        messages.add_message(request, constants.SUCCESS, 'Empresa excluida com sucesso')
        return redirect('empresas')

def empresa(request, pk):
    empresaUnica = get_object_or_404(Empresa, id=pk)
    empresas = Empresa.objects.all()
    status = Vagas.choices_status
    experiencia = Vagas.choices_experiencia
    tecnologias = Tecnologia.objects.all()
    vagas = Vagas.objects.filter(empresa_id=id)
    return render(request, 'empresaUnica.html', {'vagas': vagas,'empresas': empresas,'empresa': empresaUnica, 'status': status, 'experiencia': experiencia, 'tecnologias': tecnologias})