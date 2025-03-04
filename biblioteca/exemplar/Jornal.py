from biblioteca.exemplar.Exemplar import Exemplar

class Jornal(Exemplar):
    """Classe que representa um jornal e estende
       a classe Exemplar. 

    Atributos:
        titulo (str): O título do jornal.
        codigo (str): O código do jornalr.
    """
    def __init(self, titulo, codigo):
        super().__init__(titulo, codigo)

    def get_tipo_exemplar(self):
        """Acessa o tipo de exemplar.

        Retorna:
            str: O tipo de exemplar.
        """
        return "Jornal"    