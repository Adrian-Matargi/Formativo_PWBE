<h1 align="center">📚 Sistema de Reservas Acadêmicas – API Django</h1> <p align="center"> Uma API RESTful robusta para gerenciamento de <strong>salas, reservas, disciplinas</strong> e <strong>usuários acadêmicos</strong>, com autenticação JWT e controle de permissões. </p> <p align="center"> <img src="https://img.shields.io/badge/Django-4.x-green?style=flat-square&logo=django" /> <img src="https://img.shields.io/badge/DRF-REST--API-blue?style=flat-square&logo=python" /> <img src="https://img.shields.io/badge/MySQL-Database-orange?style=flat-square&logo=mysql" /> <img src="https://img.shields.io/badge/JWT-Authentication-yellow?style=flat-square&logo=json" /> </p>
✅ Funcionalidades
🔐 Autenticação e autorização com JWT

👥 Gerenciamento de usuários (gestores e professores)

📘 Cadastro e listagem de disciplinas

🏫 Administração de salas físicas

📅 Agendamento e controle de reservas

🚫 Prevenção automática de conflitos de horário

🔎 Filtros e visualizações baseados no tipo de usuário

🚀 Tecnologias Utilizadas
Python 3.10+

Django 4.x

Django REST Framework

Simple JWT

MySQL

python-decouple

⚠️ Certifique-se de ter o Python e o MySQL instalados antes de iniciar o projeto.

📦 Instalação
1️⃣ Clone o repositório
bash
Copiar
Editar
git clone https://github.com/Adrian-Matargi/Formativo_PWBE.git
cd Formativo_PWBE
2️⃣ Crie e ative o ambiente virtual
<details> <summary><strong>Windows</strong></summary>
bash
Copiar
Editar
python -m venv env
env\Scripts\activate
</details> <details> <summary><strong>Linux / macOS</strong></summary>
bash
Copiar
Editar
python3 -m venv env
source env/bin/activate
</details>
3️⃣ Instale as dependências
bash
Copiar
Editar
pip install -r requirements.txt
4️⃣ Configure o arquivo .env
Crie um arquivo .env na raiz do projeto com as variáveis:

env
Copiar
Editar
DEBUG=True
SECRET_KEY=sua_chave_secreta
DB_NAME=nome_do_banco
DB_USER=usuario_mysql
DB_PASSWORD=senha_mysql
DB_HOST=localhost
DB_PORT=3306
5️⃣ Execute as migrações
bash
Copiar
Editar
python manage.py makemigrations
python manage.py migrate
6️⃣ Crie um superusuário
bash
Copiar
Editar
python manage.py createsuperuser
7️⃣ Inicie o servidor
bash
Copiar
Editar
python manage.py runserver
🔑 Autenticação
A API utiliza o padrão JWT (JSON Web Token) para autenticação.

🔗 Endpoints de autenticação:
Método	Endpoint	Descrição
POST	/api/token/	Gera token de acesso
POST	/api/token/refresh/	Atualiza o token de acesso

Exemplo de uso:

http
Copiar
Editar
Authorization: Bearer <seu_token>
📌 Endpoints Principais
Recurso	Método	Endpoint	Descrição
Usuários	GET / POST	/usuarios/	Lista ou cadastra usuários
Disciplinas	GET / POST	/disciplinas/	Lista ou cadastra disciplinas
Salas	GET / POST	/salas/	Gerencia as salas disponíveis
Reservas	GET / POST	/reservas/	Cria e visualiza reservas

🧪 Executar Testes
bash
Copiar
Editar
python manage.py test
🤝 Contribuindo
Contribuições são sempre bem-vindas!
Sinta-se à vontade para abrir issues ou enviar um pull request com melhorias.

📄 Licença
Este projeto está licenciado sob os termos da MIT License.
Consulte o arquivo LICENSE para mais detalhes.
