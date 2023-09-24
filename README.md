# StudentControl API

Esta é uma API para gerenciar informações de estudantes, disciplinas e tarefas.

## Modelos

A API inclui os seguintes modelos de dados:

- `Student`: Representa informações sobre estudantes, incluindo nome e email.
- `Discipline`: Representa informações sobre disciplinas, incluindo nome e descrição.
- `Task`: Representa informações sobre tarefas, incluindo título, descrição, data de vencimento, status, associação a estudantes e relação com disciplinas.

## Endpoints da API

A API oferece os seguintes endpoints:

- `/student/`: Lista todos os estudantes e permite criar um novo estudante.
- `/student/<int:pk>/`: Obtém detalhes de um estudante específico, atualiza ou exclui o estudante.
- `/discipline/`: Lista todas as disciplinas e permite criar uma nova disciplina.
- `/discipline/<int:pk>/`: Obtém detalhes de uma disciplina específica, atualiza ou exclui a disciplina.
- `/task/`: Lista todas as tarefas e permite criar uma nova tarefa.
- `/task/<int:pk>/`: Obtém detalhes de uma tarefa específica, atualiza ou exclui a tarefa.
- `/student/<int:student_id>/tasks/`: Obtém todas as tarefas associadas a um estudante específico.

## Uso

Para usar esta API, você pode fazer solicitações HTTP para os endpoints correspondentes usando o arquivo JSON PostmanUrls utilizando do Postman.

## Instalação

1. Clone este repositório;
2. Configure seu ambiente Python (.env);
3. Instale as dependências com `pip install -r requirements.txt`;
4. Execute as migrações do banco de dados com `python manage.py migrate`;
5. Inicie o servidor de desenvolvimento com `python manage.py runserver`.