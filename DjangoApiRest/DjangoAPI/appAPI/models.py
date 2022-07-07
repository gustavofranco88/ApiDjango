from operator import truediv
from turtle import done
from venv import create
from django.db import models

# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=50)
    done = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    
class Agendamento(models.Model):
    agen_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=40)
    telefone = models.CharField(max_length=11)
    servico = models.CharField(max_length=50)
    data = models.CharField(max_length=20)#DateField('data', null=True, blank=True)
    hora = models.CharField(max_length=20)

class Usuario(models.Model):
    user_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=40)
    senha = models.CharField(max_length=20)