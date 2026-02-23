# %%
# Classe genérica e classe especializada

class NomeClasse(object):
    def __init__(self, params):
        self.atributo1 = ...
        self.atributo2 = ...
    
    def metodo1(self):
        ...

    def metodo2(self):
        ...

class NomeClasseEspecializada(NomeClasse):
    def __init__(self, params):
        super().__init__(self, params)
        self.atributo3 = ...
        self.atributo4 = ...

    def metodo3(self, params):
        ...

    def metodo4(self, params):
        ...
# %%
# Exemplo classe Estudante herdando classe Pessoa
class Pessoa(object):
    def __init__(self, nome: str, idade: int, documento: str = None):
        self.nome = nome
        self.idade = idade
        self.documento = documento

    def falar(self, texto: str) -> None:
        print(texto)

    def __str__(self) -> str:
        return f'{self.nome}, {self.idade} anos e documento número {self.documento}'
    
class Universidade(object):
    def __init__(self, nome: str):
        self.nome = nome

class Estudante(Pessoa):
    def __init__(self, nome: str, idade: int, documento: str, universidade: Universidade):
        super().__init__(nome = nome, idade=idade, documento=documento)
        self.universidade = universidade

usp = Universidade(nome='Universidade de São Paulo')
joao = Estudante(nome='João da Silva', idade=30, documento='123', universidade=usp)

print(joao)
print(joao.universidade.nome)
# %%
