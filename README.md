Design Team Flow - Sistema Kanban com Django

Índice

Configuração do Ambiente

Estrutura do Projeto

Implementação das Funcionalidades

Endpoints da API

Execução Local

Deploy

Configuração do Ambiente

1. Pré-requisitos

Certifique-se de ter o Python instalado:

python --version


2. Clonar o repositório

git clone [https://github.com/seu-usuario/API_Django.git](https://github.com/seu-usuario/API_Django.git)
cd API_Django


3. Criar Ambiente Virtual

Windows:

python -m venv venv
venv\Scripts\activate


Linux/Mac (Codespaces):

python -m venv venv
source venv/bin/activate


Nota: Você deve ver o nome do ambiente virtual (venv) no início da linha de comando quando estiver ativo.

4. Instalar Dependências

Em vez de Poetry, este projeto utiliza o pip padrão com um arquivo de requisitos para facilitar o deploy no Render.

pip install -r requirements.txt


Estrutura do Projeto

A organização segue as boas práticas do Django (MTV), separando configurações globais da lógica de negócio.

projeto_django/
├── .venv/                    # Ambiente Virtual
├── db.sqlite3                # Banco de Dados (Desenvolvimento)
├── manage.py                 # Utilitário de comando do Django
├── requirements.txt          # Lista de bibliotecas
├── build.sh                  # Script de deploy para o Render
├── setup/                    # (Pasta do PROJETO Principal)
│   ├── __init__.py
│   ├── settings.py           # Configurações globais (Apps, DB, Middleware)
│   ├── urls.py               # Rotas principais (Admin, API, Home)
│   └── wsgi.py               # Entrada para servidor web
└── apps/                     # (Pasta de APLICAÇÕES)
    └── core/                 # (App Principal: Gestão de Tarefas)
        ├── templates/        # Arquivos HTML
        │   └── interface_kanban.html
        ├── admin.py          # Configuração do painel administrativo
        ├── models.py         # Modelo do Banco de Dados (Tabela Tarefa)
        ├── serializers.py    # Conversão de Dados (Model <-> JSON)
        ├── views.py          # Lógica da API (ViewSets)
        └── urls.py           # Rotas específicas do App


setup/ - Pasta do PROJETO Django

Esta é a pasta principal do projeto Django que contém:

settings.py - Configurações globais, segurança (CSRF, CORS) e apps instalados.

urls.py - Roteamento geral (Define que / carrega o Kanban e /api/ carrega os dados).

apps/core/ - Pasta da APLICAÇÃO

Esta é a aplicação específica que contém a lógica do Kanban:

models.py - Estrutura de dados (Tarefas, Tags, Prazos).

views.py - Lógica da API REST (GET, POST, PUT, DELETE).

templates/ - Interface visual (HTML + TailwindCSS + JS).

Implementação das Funcionalidades

1. Configurar settings.py

Editamos setup/settings.py para incluir as apps e configurações de segurança para o deploy:

INSTALLED_APPS = [
    # ... apps padrão ...
    'rest_framework', # API
    'corsheaders',    # Segurança de acesso
    'apps.core',      # Nossa aplicação
]

# Configuração para arquivos estáticos no Render
STATIC_ROOT = BASE_DIR / 'staticfiles'


2. Criar Modelo (apps/core/models.py)

O modelo Tarefa suporta tags e status para o Kanban:

from django.db import models

class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('TODO', 'A Fazer'),
        ('DOING', 'Em Andamento'),
        ('DONE', 'Concluído'),
    ]
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True, null=True) # Ex: "Urgente, Instagram"
    prazo = models.DateTimeField()
    status = models.CharField(max_length=5, choices=STATUS_CHOICES, default='TODO')
    criado_em = models.DateTimeField(auto_now_add=True)


3. Criar Serializer (apps/core/serializers.py)

Converte o modelo Python para JSON, permitindo que o Frontend (JavaScript) entenda os dados.

from rest_framework import serializers
from .models import Tarefa

class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = '__all__'


4. Interface Kanban (Templates)

O arquivo interface_kanban.html implementa:

Drag & Drop: API HTML5 nativa para arrastar cartões.

Polling: Atualização automática a cada 3 segundos.

Filtros: Busca por texto, data e navegação por mês.

Design: Estilização responsiva com TailwindCSS.

Endpoints da API

O sistema expõe uma API REST completa em /api/tarefas/.

Método

Endpoint

Descrição

GET

/api/tarefas/

Lista todas as tarefas (JSON)

POST

/api/tarefas/

Cria uma nova tarefa

GET

/api/tarefas/{id}/

Detalhes de uma tarefa específica

PUT

/api/tarefas/{id}/

Atualiza uma tarefa completa

PATCH

/api/tarefas/{id}/

Atualiza parcial (ex: mudar status ao arrastar)

DELETE

/api/tarefas/{id}/

Remove uma tarefa

Execução Local

1. Aplicar migrações

Cria o banco de dados SQLite localmente:

python manage.py makemigrations
python manage.py migrate


2. Criar Superusuário (Opcional)

Para acessar o painel administrativo (/admin):

python manage.py createsuperuser


3. Executar servidor

python manage.py runserver


4. Acessar o site

Kanban: http://127.0.0.1:8000/

Admin: http://127.0.0.1:8000/admin/

Deploy

O projeto está configurado para deploy automático na plataforma Render.

Arquivos de Configuração

requirements.txt: Lista o gunicorn (servidor de produção) e bibliotecas.

build.sh: Script que instala dependências e roda migrações automaticamente no servidor.

#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate


Desenvolvido como Projeto Integrador de Desenvolvimento Web.
