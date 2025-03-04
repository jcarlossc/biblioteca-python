class Usuario:
    """Classe que representa um usuário e tem a
       função de ser a classe mãe das classes
       Aluno, Professor e Funcionário. 

    Atributos:
        nome (str): O nome do usuário.
        cpf (str): O cpf do usuário.
    """
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def get_nome(self):
        """Acessa o nome do usuário.

        Retorna:
            str: O nome de usuário.
        """
        return self.nome

    def get_cpf(self):
        """Acessa o cpf de usuário.

        Retorna:
            str: O cpf de usuário.
        """
        return self.cpf 

    def __str__(self):
        """Acessa uma representação dos atributos de usuário.

        Retorna:
            str: O nome e cpf do usuário.
        """
        return f"{self.get_nome} || {self.get_cpf}"   