from datetime import datetime, timedelta

class Emprestimo:
    def __init__(self, usuario):
        self.usuario = usuario
        self.emprestimos = []
        self.data_hora = datetime.now()

    def get_usuario(self):
        return self.usuario

    def add_emprestimo(self, exemplar):
        devolucao = self.data_hora + timedelta(days=10)
        emprestimo = {
            "Título" : exemplar.get_titulo(),
            "Tipo" : exemplar.get_tipo_exemplar(),
            "Data da Devolução" : devolucao.strftime("%d/%m/%Y")
        }
        self.emprestimos.append(emprestimo)

    def get_emprestimos(self):
        print("------------------------------------ EMPRÉSTIMOS -----------------------------------")
        print("Usuário:", self.usuario.get_nome())
        print("Cpf:", self.usuario.get_cpf())
        print("Tipo de usuário:", self.usuario.get_tipo_usuario())
        print("Data do empréstimo:", self.data_hora.strftime("%d/%m/%Y"))
        print("Hora do empréstimo:", self.data_hora.strftime("%H:%M:%S"))
        print("--- Lista de Empréstimos ---")
        for impressao in self.emprestimos:
            print(impressao)   
        print("-------------------------------------- FIM -----------------------------------------")