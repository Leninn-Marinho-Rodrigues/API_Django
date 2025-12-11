from django.contrib import admin
from .models import Tarefa

# Isso permite gerenciar as tarefas pela interface administrativa do Django (/admin)
@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'status', 'prazo', 'criado_em')
    list_filter = ('status', 'prazo')
    search_fields = ('titulo', 'descricao')