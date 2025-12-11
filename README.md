# Design Team Flow — Sistema Kanban com Django

> Projeto integrador de Desenvolvimento Web: um Kanban simples, responsivo e com API REST em Django + DRF.

**Sumário**
- [Visão Geral](#visão-geral)
- [Configuração do Ambiente](#configuração-do-ambiente)
  - [Pré-requisitos](#pré-requisitos)
  - [Clonar o repositório](#clonar-o-repositório)
  - [Criar ambiente virtual](#criar-ambiente-virtual)
  - [Instalar dependências](#instalar-dependências)
- [Estrutura do Projeto](#estrutura-do-projeto)
  - [setup/ — Projeto Django](#setup--—-projeto-django)
  - [apps/core/ — Aplicação Kanban](#appscore--—-aplicação-kanban)
- [Implementação das Funcionalidades](#implementação-das-funcionalidades)
  - [1) Configurar `settings.py`](#1-configurar-settingspy)
  - [2) Modelo `Tarefa` (`models.py`)](#2-modelo-tarefa-modelspy)
  - [3) Serializer (`serializers.py`)](#3-serializer-serializerspy)
  - [4) Interface Kanban (`templates/`)](#4-interface-kanban-templates)
- [Endpoints da API](#endpoints-da-api)
- [Execução Local](#execução-local)
- [Deploy no Render](#deploy-no-render)
  - [Arquivos de configuração](#arquivos-de-configuração)
  - [Script `build.sh`](#script-buildsh)
- [Licença e créditos](#licença-e-créditos)
- [Referências](#referências)

---

## Visão Geral

O **Design Team Flow** é um sistema Kanban para gestão de tarefas, com arrastar-e-soltar (HTML5), atualização periódica (polling) e filtros por texto e data. Backend em **Django** + **Django REST Framework** e frontend com **Tailwind CSS**.

---

## Configuração do Ambiente

### Pré-requisitos
- **Python** instalado:
```bash
python --version
```

### Clonar o repositório
```bash
git clone https://github.com/Leninn-Marinho-Rodrigues/API_Django.git
cd API_Django
```

### Criar ambiente virtual
**Windows**
```bash
python -m venv venv
venv\Scripts ctivate
```

**Linux/Mac (incluindo Codespaces)**
```bash
python -m venv venv
source venv/bin/activate
```

> Dica: ao ativar, você verá `(venv)` no início da linha de comando.

### Instalar dependências
Este projeto usa **pip** com `requirements.txt` (facilita o deploy no Render):
```bash
pip install -r requirements.txt
```

---

## Estrutura do Projeto

Segue a organização baseada nas boas práticas MTV do Django, separando configurações globais da lógica de negócio:

```text
projeto_django/
├── .venv/                 # Ambiente virtual
├── db.sqlite3             # Banco de dados (desenvolvimento)
├── manage.py              # Utilitário de comando do Django
├── requirements.txt       # Lista de bibliotecas (pip)
├── build.sh               # Script de deploy para o Render
├── setup/                 # Pasta do PROJETO principal
│   ├── __init__.py
│   ├── settings.py        # Configurações globais (Apps, DB, Middleware)
│   ├── urls.py            # Rotas principais (Admin, API, Home)
│   └── wsgi.py            # Entrada para servidor web
└── apps/                  # Pasta de APLICAÇÕES
    └── core/              # App principal: Gestão de Tarefas
        ├── templates/     # Arquivos HTML
        │   └── interface_kanban.html
        ├── admin.py       # Configuração do painel administrativo
        ├── models.py      # Modelo do banco (Tabela Tarefa)
        ├── serializers.py # Conversão de dados (Model <-> JSON)
        ├── views.py       # Lógica da API (ViewSets)
        └── urls.py        # Rotas específicas do App
```

### `setup/` — Projeto Django
- `settings.py`: apps instalados, segurança (CSRF/CORS), estáticos e banco.
- `urls.py`: roteamento geral — `/` carrega o Kanban e `/api/` expõe dados.

### `apps/core/` — Aplicação Kanban
- `models.py`: estrutura de dados (Tarefas, Tags, Prazos).
- `views.py`: API REST (GET, POST, PUT, PATCH, DELETE).
- `templates/`: interface visual com **Tailwind CSS** + JS.

---

## Implementação das Funcionalidades

### 1) Configurar `settings.py`
Instale as apps e ajuste segurança para deploy:

```python
INSTALLED_APPS = [
    # ... apps padrão ...
    'rest_framework',   # API
    'corsheaders',      # Segurança de acesso
    'apps.core',        # Nossa aplicação
]

# Arquivos estáticos (Render)
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

### 2) Modelo `Tarefa` (`models.py`)
Suporta tags e status Kanban:

```python
from django.db import models

class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('TODO', 'A Fazer'),
        ('DOING', 'Em Andamento'),
        ('DONE', 'Concluído'),
    ]

    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True, null=True)  # Ex: "Urgente, Instagram"
    prazo = models.DateTimeField()
    status = models.CharField(max_length=5, choices=STATUS_CHOICES, default='TODO')
    criado_em = models.DateTimeField(auto_now_add=True)
```

### 3) Serializer (`serializers.py`)
Converte modelo Python ↔ JSON para consumo no frontend:

```python
from rest_framework import serializers
from .models import Tarefa

class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = '__all__'
```

### 4) Interface Kanban (`templates/`)
`interface_kanban.html` implementa:
- **Drag & Drop** nativo (HTML5) para arrastar cartões  
- **Polling**: atualização automática a cada 3s  
- **Filtros**: busca por texto, data e navegação por mês  
- **Design**: estilização responsiva com **Tailwind CSS**

---

## Endpoints da API

Base URL (dev): `http://127.0.0.1:8000/api/`

| Método | Endpoint             | Descrição                                          |
|:------:|----------------------|----------------------------------------------------|
| GET    | `/api/tarefas/`      | Lista todas as tarefas (JSON)                     |
| POST   | `/api/tarefas/`      | Cria uma nova tarefa                              |
| GET    | `/api/tarefas/{id}/` | Detalhes de uma tarefa específica                 |
| PUT    | `/api/tarefas/{id}/` | Atualiza uma tarefa completa                      |
| PATCH  | `/api/tarefas/{id}/` | Atualiza parcial (ex.: mudar status ao arrastar)  |
| DELETE | `/api/tarefas/{id}/` | Remove uma tarefa                                 |

> Permissões e autenticação podem ser ajustadas via DRF conforme necessidade.

---

## Execução Local

1) **Aplicar migrações**  
```bash
python manage.py makemigrations
python manage.py migrate
```

2) **Criar superusuário (opcional)**  
```bash
python manage.py createsuperuser
```

3) **Rodar servidor**  
```bash
python manage.py runserver
```

4) **Acessar o site**  
- Kanban: `http://127.0.0.1:8000/`  
- Admin: `http://127.0.0.1:8000/admin/`

---

## Deploy no Render

Projeto preparado para deploy automático no **Render** com coleta de estáticos e migrações.

### Arquivos de configuração
- `requirements.txt`: inclui `gunicorn` e bibliotecas do projeto.
- `build.sh`: instala dependências e executa migrações no servidor.

### Script `build.sh`
```bash
#!/usr/bin/env bash

# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
```

---

## Licença e créditos

- Desenvolvido como **Projeto Integrador de Desenvolvimento Web**.
- Repositório: https://github.com/Leninn-Marinho-Rodrigues/API_Django

---

## Referências

- README do professor (organização por seções e sumário): https://github.com/claulis/Py/blob/main/DJ/readme.md  
- Boas práticas de README (estrutura e seções úteis): https://realpython.com/readme-python-project/
