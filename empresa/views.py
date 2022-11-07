from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def novaEmpresa(request):
    return render(request, 'novaEmpresa.html')