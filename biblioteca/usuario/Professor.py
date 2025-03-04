from biblioteca.usuario.Usuario import Usuario

class Professor(Usuario):
    """Classe que representa um professor e estende a classe Usuário.

    Atributos:
        nome (str): O nome do professor.
        cpf (str): O cpf do professor.
    """
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)

    def get_tipo_usuario(self):
        """Acessa o tipo de usuário.

        Retorna:
            str: O tipo de usuário.
        """
        return "Professor"  