from biblioteca.usuario.Usuario import Usuario

class Professor(Usuario):
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)

    def get_tipo_usuario(self):
        return "Professor"  