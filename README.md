# Estudo sobre orientação a objetos em linguagem de programação Python e ambiente VENV.

VENV: Um ambiente virtual em Python isola dependências do projeto, evitando conflitos com pacotes globais do sistema. Ele permite que cada projeto tenha suas próprias bibliotecas e versões específicas.

Este é um projeto simples que simula uma biblioteca de empréstimos de exemplares de livros, revistas e jornais.
Ele é composto por nove classes que estão distribuídas em três pacotes: o pacote usuário, que contém as classes Aluno, Professor e Funcionário que estendem a classe Usuário; o pacote exemplar, que contém as classes Livro, Revista e Jornal que estendem a classe Exemplar; e a classe Empréstimo, que centraliza os empréstimos.

## FERRAMENTAS UTILIZADAS
* Linguagem de programação Python.
* Ambiente virtual VENV.
* Git/GitHub
* Visual studio code.
* Windows 10.

## MODO DE UTILIZAR
* Clonar repositório.
* No diretório 'biblioteca-python', executar ```python -m venv venv``` para instalar o ambiente virtual.
* Executar ```pip install -r requirements.txt``` para instalar as dependências. Obs: Este projeto não contém dependências.
* Executar, caso esteja no Windows, ```venv\Scripts\activate``` para iniciar o ambiente. Caso Linux ou MacOS, ```source venv/bin/activate```.
* ```python app.py``` - Executa o algoritmo.
* Para sair do ambiente virtual ```deactivate```.

## COMANDOS IMPORTANTES
* ```python -m venv venv``` - Cria um ambiente virtual chamado venv. Observação: o primeiro venv é o comando, o segundo, o nome do diretório.
* No Windows, ```venv\Scripts\activate``` e no Linux, ```source venv/bin/activate``` - Inicializa o ambiente.
* ```deactivate``` - Encerra o ambiente.
* ```pip freeze > requirements.txt``` - Gera o arquivo que contém dependências. Esse mesmo comando atualiza o arquivo.
* ```pip list``` - Lista as dependências do projeto.
* ```pip show``` - Inserindo o nome da dependência após o comando, lista informações da dependência.
* ```pip install -r requirements.txt``` - Instala dependências que estão no arquivo 'requirements.txt'.
* ```pip install``` - Inserindo o nome da dependência após o comando, instala dependências.
* ```pip uninstall``` - Inserindo o nome da dependência após o comando, desinstala dependências.