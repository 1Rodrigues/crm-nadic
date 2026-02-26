objetivo:
Crie um mecanismo de CRM (o que é CRM: ( [wikipedia link](https://pt.wikipedia.org/wiki/Sistemas_de_CRM) ) para qualquer tipo de empresa, onde será possível cadastrar/remover/editar produtos, assim como definir quantidade em estoque e sempre que realizado uma venda o estoque e o faturamento total da empresa deve ser atualizado.

##  Funcionalidades

- **Gerenciamento de Produtos**: CRUD completo (Criação, Leitura, Atualização e Deleção) de produtos com controle de estoque.
- **Sistema de Vendas**: Registro de itens de venda com atualização automática de estoque após a conclusão.
- **Dashboard**: Visualização em tempo real do faturamento total e quantidade de vendas realizadas.
- **Interface Responsiva**: Utiliza Bootstrap 5 para garantir uma boa experiência em diferentes dispositivos.

##  Tecnologias Utilizadas

- **Framework Web**: Django 6.0.2
- **Banco de Dados**: PostgreSQL
- **Frontend**: HTML5, CSS3 (Bootstrap 5)
- **Linguagem**: Python 3

##  Pré-requisitos

- Python 3.10 ou superior
- PostgreSQL
- Git

##  Instalação e Configuração

### 1. Clonar o Repositório

git clone <url-do-seu-repositorio>
cd crm-nadic

2. Configurar o Ambiente Virtual
Bash

python -m venv venv
# No Linux/macOS:
source venv/bin/activate
# No Windows:
venv\Scripts\activate

3. Instalar Dependências
Bash

pip install django psycopg2-binary

4. Configurar o Banco de Dados

O projeto está configurado para usar o PostgreSQL com as seguintes credenciais:

    Database: crm

    User: crm_user

    Password: 1234

    Host: localhost

    Port: 5432

Certifique-se de que o banco de dados 'crm' exista no seu PostgreSQL antes de prosseguir.
5. Executar Migrações
Bash

python manage.py migrate

6. Criar Superusuário (Acesso ao Admin)
Bash

python manage.py createsuperuser

7. Iniciar o Servidor
Bash

python manage.py runserver
