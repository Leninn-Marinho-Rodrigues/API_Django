from django.test import TestCase
from .models import Tarefa
from django.utils import timezone

class TarefaModelTest(TestCase):
    def setUp(self):
        # Cria uma tarefa de exemplo antes de cada teste
        self.tarefa = Tarefa.objects.create(
            titulo="Teste Unitário",
            descricao="Verificando se o Django salva corretamente",
            prazo=timezone.now(),
            status="TODO"
        )

    def test_criacao_tarefa(self):
        """Testa se a tarefa foi criada com o título correto"""
        self.assertEqual(self.tarefa.titulo, "Teste Unitário")
        self.assertEqual(self.tarefa.status, "TODO")
        print("\n✅ Teste de criação de tarefa: SUCESSO")

    def test_str_representation(self):
        """Testa se o nome da tarefa aparece corretamente (def __str__)"""
        esperado = "Teste Unitário (A Fazer)"
        self.assertEqual(str(self.tarefa), esperado)
        print("✅ Teste de representação de string: SUCESSO")