# 🧩 Design Team Flow — API REST com Django

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-0A0A0A?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![pip](https://img.shields.io/badge/pip-3775A9?style=for-the-badge&logo=pypi&logoColor=white)
![Gunicorn](https://img.shields.io/badge/Gunicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=000)

</div>

> API RESTful desenvolvida com Django e Django REST Framework para gerenciamento de tarefas de um time de design.

---

## 📘 Visão Geral

O **Design Team Flow** é uma API backend que permite **criar, listar, atualizar e excluir tarefas**.  
Ideal para integrar com sistemas Kanban, dashboards ou qualquer aplicação de gestão de demandas.

---

## ⚙️ Configuração do Ambiente

### ✅ Pré-requisitos

- Python instalado:
```bash
python --version
📥 Clonar o repositório
git clone https://github.com/Leninn-Marinho-Rodrigues/API_Django.git
cd API_Django


🧪 Criar ambiente virtual
Windows
python -m venv venv
venv\Scripts\activate


Linux/Mac
python -m venv venv
source venv/bin/activate


📦 Instalar dependências
pip install -r requirements.txt



📁 Estrutura do Projeto
projeto_django/
├── manage.py
├── requirements.txt
├── build.sh
├── db.sqlite3
├── setup/
│   ├── settings.py
│   └── urls.py
└── apps/
    └── core/
        ├── models.py
        ├── views.py
        ├── serializers.py
        └── urls.py



🧩 Implementação das Funcionalidades
🔧 Modelo Tarefa (models.py)
class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('TODO', 'A Fazer'),
        ('DOING', 'Em Andamento'),
        ('DONE', 'Concluído'),
    ]

    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True, null=True)
    prazo = models.DateTimeField()
    status = models.CharField(max_length=5, choices=STATUS_CHOICES, default='TODO')
    criado_em = models.DateTimeField(auto_now_add=True)



🔄 Serializer (serializers.py)
class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = '__all__'



🔁 ViewSet (views.py)
class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer



🔗 Endpoints da API
Base URL: http://127.0.0.1:8000/api/
|  |  |  | 
|  | /api/tarefas/ |  | 
|  | /api/tarefas/ |  | 
|  | /api/tarefas/{id}/ |  | 
|  | /api/tarefas/{id}/ |  | 
|  | /api/tarefas/{id}/ |  | 
|  | /api/tarefas/{id}/ |  | 



▶️ Execução Local
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser  # opcional
python manage.py runserver


- API: http://127.0.0.1:8000/api/
- Admin: http://127.0.0.1:8000/admin/
- Swagger: http://127.0.0.1:8000/

🚀 Deploy no Render
Projeto preparado para deploy automático com coleta de estáticos e migrações.
Arquivos de configuração
- requirements.txt — inclui gunicorn e dependências
- build.sh — script de inicialização
#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate



📄 Licença e Créditos
- Desenvolvido por Leninn Marinho Rodrigues como parte do Projeto Integrador de Desenvolvimento Web.
- Repositório: GitHub
