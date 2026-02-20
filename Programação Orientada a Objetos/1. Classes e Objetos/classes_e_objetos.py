# %%
# Definição de classe

class NomeClasse(object):

    def __init__ (self, params):
        self.atributo1 = ...
        self.atributo2 = ...

    def metodo1(self, params):
        ...

    def metodo2(self, params):
        ...

# %%
# Exemplo de classe: Pessoa
from time import sleep

class Pessoa(object):

    def __init__(self, nome: str, idade: int, documento: str = None):
        self.nome = nome
        self.idade = idade
        self.documento = documento

    def dormir(self, horas: int) -> None:
        for hora in range(1, horas+1):
            print(f'Dormindo por {hora} horas')
            sleep(1)

    def falar(self, texto: str) -> None:
        print(texto)

    def __str__(self) -> str:
        return f'{self.nome}, {self.idade} anos e documento número {self.documento}'
# %%
# Instanciação de Objetos
joao = Pessoa(nome='João da Silva', idade=20, documento='123')
maria = Pessoa(nome='Maria dos Santos', idade=25, documento='456')
jose = Pessoa(nome='José Alves', idade=1)

print(joao.nome)
# %%
# Exemplos de manipulação
def maior_de_idade(idade: int) -> bool:
    return idade >= 18

if maior_de_idade(idade=jose.idade):
    print(f'{jose.nome} é maior de idade')
else:
    print(f'{jose.nome} não é maior de idade')

score_credito = {'123': 750, '456': 850, '678': 950}

score = score_credito[maria.documento]
print(score)

print(joao)
print(type(joao))
joao.dormir(horas=2)
joao.falar(texto=f'Olá pessoal! Aqui é o {joao.nome}')
# %%
# Exemplo classe arquivo CSV
class ArquivoCSV(object):
    def __init__(self, arquivo: str):
        self.arquivo = arquivo
        self.conteudo = self._extrair_conteudo()
        self.colunas = self._extrair_nome_colunas()

        def _extrair_conteudo(self):
            conteudo = None
            with open(file=self.arquivo, mode='r', encoding='utf-8') as arquivo:
                conteudo = arquivo.readlines()
            return conteudo
        
        def _extrair_nome_colunas(self):
            return self.conteudo[0].strip().split(sep=',')
        
        def extrair_coluna(self, indice_coluna: str):
            coluna = list()
            for linha in self.conteudo:
                conteudo_linha = linhha.strip().split(sep=',')
                coluna.append(conteudo_linha[indice_coluna])
            coluna.pop(0)
            return coluna