from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tecnologia

# Create your views here.

def novaEmpresa(request):
    techs = Tecnologia.objects.all()
    return render(request, 'novaEmpresa.html', {'techs': techs})