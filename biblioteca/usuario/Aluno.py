from biblioteca.usuario.Usuario import Usuario

class Aluno(Usuario):
    """Classe que representa um aluno e estende a classe Usuário.

    Atributos:
        nome (str): O nome do aluno.
        cpf (str): O cpf do aluno.
    """
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)

    def get_tipo_usuario(self):
        """Acessa o tipo de usuário.

        Retorna:
            str: O tipo de usuário.
        """
        return "Aluno"    