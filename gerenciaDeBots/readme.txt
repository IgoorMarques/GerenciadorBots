

Configuração do Ambiente
Configurar Ambiente Virtual

    python -m venv nome_do_ambiente
    source nome_do_ambiente/bin/activate  # Unix/MacOS
    nome_do_ambiente\Scripts\activate  # Windows


Instalar Dependências
Instale todas as dependências necessárias executando:

    pip install -r requirements.txt

Executando o Projeto
Para iniciar o servidor do Django, execute:

    1 - cd Gerenciador_bots_telegram
    2 - python manage.py runserver


Criar um Superusuário:
    python manage.py createsuperuser

Migrações

    python manage.py makemigrations
    python manage.py migrate

