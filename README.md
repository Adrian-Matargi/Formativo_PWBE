<h1 align="center">📚 Sistema de Reservas Acadêmicas – API Django</h1>

<p align="center">
  Uma API RESTful robusta para gerenciamento de <strong>salas, reservas, disciplinas</strong> e <strong>usuários acadêmicos</strong>, com autenticação JWT e controle de permissões.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Django-4.x-green?style=flat-square&logo=django" />
  <img src="https://img.shields.io/badge/DRF-REST--API-blue?style=flat-square&logo=python" />
  <img src="https://img.shields.io/badge/MySQL-Database-orange?style=flat-square&logo=mysql" />
  <img src="https://img.shields.io/badge/JWT-Authentication-yellow?style=flat-square&logo=json" />
</p>

---

## ✅ Funcionalidades

- 🔐 Autenticação e autorização com **JWT**
- 👥 Gerenciamento de **usuários** (gestores e professores)
- 📘 Cadastro e listagem de **disciplinas**
- 🏫 Administração de **salas físicas**
- 📅 Agendamento e controle de **reservas**
- 🚫 Prevenção automática de **conflitos de horário**
- 🔎 Filtros e visualizações baseados no tipo de usuário

---

## 🚀 Tecnologias Utilizadas

- **Python 3.10+**
- **Django 4.x**
- **Django REST Framework**
- **Simple JWT**
- **MySQL**
- **python-decouple**

> ⚠️ Certifique-se de ter o **Python** e o **MySQL** instalados antes de iniciar o projeto.

---

## 📦 Instalação

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/Adrian-Matargi/Formativo_PWBE.git
cd Formativo_PWBE
```

### 2️⃣ Crie e ative o ambiente virtual

```bash
python -m venv env
env\Scripts\activate
```

### 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure o banco de dados

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'formativo', #Nome do banco de dados
        'USER' : 'root', #Nome do usuário 
        'PASSWORD' : 'senai', #Senha do banco de dados
        'HOST' : 'localhost', #Endereço
        'PORT' : '3306' #Porta em que o banco será executado
    }
}
```

### 5️⃣ Execute as migrações do banco de dados

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Crie um superusuário

```bash
python manage.py createsuperuser
```

### 7️⃣ Inicie o servidor de desenvolvimento

```bash
python manage.py runserver
```


## 📌 Endpoints Principais
Recurso	Método	Endpoint	Descrição

Usuários	GET / POST	/usuarios/	Lista ou cadastra usuários

Disciplinas	GET / POST	/disciplinas/	Lista ou cadastra disciplinas

Salas	GET / POST	/salas/	Gerencia as salas disponíveis

Reservas	GET / POST	/reservas/	Cria e visualiza reservas
