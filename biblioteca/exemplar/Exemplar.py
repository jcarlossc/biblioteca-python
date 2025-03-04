class Exemplar:
    def __init__(self, titulo, codigo):
        self.titulo = titulo
        self.codigo = codigo

    def get_titulo(self):
        return self.titulo

    def get_codigo(self):
        return self.codigo

    def __str__(self):
        return f"{self.get_titulo} || {self.get_codigo}"    