# Avaliação EXAPE

A maioria das aplicações precisa manter o controle de quem são seus usuários. 
O método de autenticação mais comum exige que os usuários forneçam alguma identificação, que pode ser o seu endereço de e-mail ou o nome de usuário, além de uma senha.

### Extensões de autenticação para o Flask

A solução de autenticação exigida nesta avaliação utiliza os pacotes abaixo:

- Flask-Login: gerenciamento de sessões para usuários logados
- Werkzeug: hashing e verificação de senhas
- itsdangerous: geração e verificação de tokens protegidos por criptografia

### O que será avaliado de acordo com o Projeto Pedagógico do Curso (PPC) e conteúdo programático da disciplina

- Introdução ao desenvolvimento de sistemas Web;
- Frameworks
  - Para a apresentação,
  - Para a persistência de objetos.
- Padrões de projetos;

## O resultado da avaliação deverá apresentar as funcionalidades da aplicação disponível em [Avaliação EXAPE](https://flaskaulas.pythonanywhere.com/)

- Altere apenas o arquivo app/auth/views.py do repositorio disponibilizado
- Os dados dos usuários deverão ser persistidos em banco de dados
- Publique a sua aplicação na plataforma [PythonAnywhere](https://www.pythonanywhere.com/)

# Critérios de avaliação

1. Código corretamente alterado (5 pontos)
   - Função de view `def login()`: 1,5 pontos
   - Função de view `def logout()`: 1,5 pontos
   - Função de view `def register()`: 2 pontos
2. Aplicação publicada na plataforma PythonAnyWhere
   - Execução da funcionalidade `Login`: 0,5 ponto
   - Execução da funcionalidade `Logout`: 0,5 ponto
   - Persistência em banco de dados: 2 pontos
   - Execução da funcionalidade `Registro de usuários`: 2 pontos