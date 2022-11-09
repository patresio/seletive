from django.db import models

# Create your models here.
class Tecnologia(models.Model):
    tecnologia = models.CharField(max_length=30)

    def __str__(self):
        return self.tecnologia


class Empresa(models.Model):
    choices_nicho_mercado = (
        ('M', 'Marketing'),
        ('N', 'Nutrição'),
        ('D', 'Design'),
        ('T', 'Tecnologia'),
        ('SP', 'Setor Publico'),
        ('AM', 'Agencia de Modelo')
    )
    logo = models.ImageField(upload_to="logo_empresa", null=True)
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    cidade = models.CharField(max_length=30)
    tecnologias = models.ManyToManyField(Tecnologia)
    endereco = models.CharField(max_length=30)
    caracteristica_empresa = models.TextField()
    nicho_mercado = models.CharField(max_length=3, choices=choices_nicho_mercado)

    def __str__(self):
        return self.nome

    def qtde_vagas(self):
        return Vagas.objects.filter(empresa__id=self.id).count()


class Vagas(models.Model):
    choices_experiencia = (
        ('E', 'Estagiaio'),
        ('T', 'Trainner'),
        ('F', 'FreeLancer'),
        ('J', 'Júnior'),
        ('P', 'Pleno'),
        ('S', 'Sênior')
    )

    choices_status = (
        ('I', 'Interesse'),
        ('C', 'Currículo enviado'),
        ('E', 'Entrevista'),
        ('D', 'Desafio técnico'),
        ('F', 'Finalizado')
    )
    
    empresa = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING)
    titulo = models.CharField(max_length=30)
    email = models.EmailField()
    nivel_experiencia = models.CharField(max_length=2, choices=choices_experiencia)
    data_final = models.DateField()
    status = models.CharField(max_length=30, choices=choices_status)
    tecnologias_dominadas = models.ManyToManyField(Tecnologia)
    tecnologias_estudar = models.ManyToManyField(Tecnologia, related_name='estudar')


    def __str__(self):
        return self.titulo