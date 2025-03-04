from biblioteca.exemplar.Exemplar import Exemplar

class Livro(Exemplar):
    """Classe que representa um livro e estende
       a classe Exemplar. 

    Atributos:
        titulo (str): O título do livro.
        codigo (str): O código do livro.
    """
    def __init(self, titulo, codigo):
        super().__init__(titulo, codigo)

    def get_tipo_exemplar(self):
        """Acessa o tipo de exemplar.

        Retorna:
            str: O tipo de exemplar.
        """
        return "Livro"    