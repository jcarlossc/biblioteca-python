from biblioteca.exemplar.Exemplar import Exemplar

class Jornal(Exemplar):
    def __init(self, titulo, codigo):
        super().__init__(titulo, codigo)

    def get_tipo_exemplar(self):
        return "Jornal"    