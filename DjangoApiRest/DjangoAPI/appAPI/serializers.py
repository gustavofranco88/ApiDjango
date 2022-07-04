from dataclasses import fields
from appAPI.models import Agendamento
from appAPI.models import Todo
 
from rest_framework import serializers
 
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'name', 'done', 'create_at']

class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = ['agen_id', 'nome', 'telefone', 'servico', 'data', 'hora']
        

