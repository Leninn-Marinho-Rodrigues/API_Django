from rest_framework import serializers
from .models import Tarefa

class TarefaSerializer(serializers.ModelSerializer):
    prazo_formatado = serializers.DateTimeField(source='prazo', format="%d/%m/%Y %H:%M", read_only=True)

    class Meta:
        model = Tarefa
        fields = '__all__'