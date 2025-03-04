from biblioteca.emprestimo.Emprestimo import Emprestimo
from biblioteca.exemplar.Jornal import Jornal
from biblioteca.exemplar.Revista import Revista
from biblioteca.exemplar.Livro import Livro
from biblioteca.usuario.Funcionario import Funcionario
from biblioteca.usuario.Professor import Professor
from biblioteca.usuario.Aluno import Aluno


aluno1 = Aluno("Carlos", "12345678989")
livro1 = Livro("Ecco Homo", "123456")
revista1 = Revista("Veja", "456789")
jornal1 = Jornal("Diário de Pernambuco", "781234")
emp1 = Emprestimo(aluno1)
emp1.add_emprestimo(livro1)
emp1.add_emprestimo(revista1)
emp1.add_emprestimo(jornal1)
emp1.get_emprestimos()

professor1 = Professor("Soares", "78945612399")
livro2 = Livro("A Odisseia", "235689")
revista2 = Revista("Isto É", "326598")
jornal2 = Jornal("Jornal do Comércio", "258741")
emp2 = Emprestimo(professor1)
emp2.add_emprestimo(livro2)
emp2.add_emprestimo(revista2)
emp2.add_emprestimo(jornal2)
emp2.get_emprestimos()

funcionario1 = Funcionario("Jose", "65432178966")
livro3 = Livro("Humano, Demasiado Humano", "357841")
revista3 = Revista("Super Interessante", "362589")
jornal3 = Jornal("Folha de Pernambuco", "987898")
emp3 = Emprestimo(funcionario1)
emp3.add_emprestimo(livro3)
emp3.add_emprestimo(revista3)
emp3.add_emprestimo(jornal3)
emp3.get_emprestimos()