class Exemplar:
    """Classe que representa um exemplar da biblioteca
       e tem a função de ser a classe mãe das classes
       Livro, Revista e Jornal. 

    Atributos:
        titulo (str): O título do exemplar.
        codigo (str): O código do exemplar.
    """
    def __init__(self, titulo, codigo):
        self.titulo = titulo
        self.codigo = codigo

    def get_titulo(self):
        """Acessa o título do exemplar.

        Retorna:
            str: O título do exemplar.
        """
        return self.titulo

    def get_codigo(self):
        """Acessa o código do exemplar.

        Retorna:
            str: O código do exemplar.
        """
        return self.codigo

    def __str__(self):
        """Acessa uma representação dos atributos do exemplar.

        Retorna:
            str: O título e código do exemplar.
        """
        return f"{self.get_titulo} || {self.get_codigo}"    