from django.contrib import admin
from .models import Tecnologia, Empresa, Vagas

# Register your models here.
admin.site.register(Tecnologia)
admin.site.register(Empresa)
admin.site.register(Vagas)