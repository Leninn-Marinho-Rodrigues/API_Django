from django.db import models

class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('TODO', 'A Fazer'),
        ('DOING', 'Em Andamento'),
        ('DONE', 'Concluído'),
    ]

    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    prazo = models.DateTimeField()
    status = models.CharField(max_length=5, choices=STATUS_CHOICES, default='TODO')
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} ({self.get_status_display()})"
