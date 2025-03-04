from biblioteca.exemplar.Exemplar import Exemplar

class Revista(Exemplar):
    """Classe que representa uma revista e estende
       a classe Exemplar. 

    Atributos:
        titulo (str): O título da revista.
        codigo (str): O código da revista.
    """
    def __init(self, titulo, codigo):
        super().__init__(titulo, codigo)

    def get_tipo_exemplar(self):
        """Acessa o tipo de exemplar.

        Retorna:
            str: O tipo de exemplar.
        """
        return "Revista"    