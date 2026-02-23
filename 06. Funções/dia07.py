# %%
# Funções
def mostrarLinha():
    print('-' * 30)

mostrarLinha()
# %%
mostrarLinha()
print('Funções no Python')
mostrarLinha()
# %%
# Argumentos
def titulo(texto):
    mostrarLinha()
    print(texto)
    mostrarLinha()

titulo('Funções com argumentos')
titulo('Aprendizado de Python')
titulo('Repetição de código')
# %%
def soma(a, b):
    soma = a + b
    print(f'A: {a}, B: {b}, A+B = {soma}')

soma(1, 1)
soma(2, 2)
soma(b=5, a=2)
# %%
# Funções com quantidade de argumentos indefinidos
def contador(*num):
    print(num)
    print(len(num))

contador(1, 2, 3, 4, 5)
contador(1)
contador(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# %%
def soma2(valores):
    soma = 0
    for num in valores:
        soma += num
        print(f'Somando mais {num}')
    print(f'Total = {soma}')

lista_de_numeros = [1, 5, 10, 15]

soma2(lista_de_numeros)
# %%
def dobro(valores):
    for num in valores:
        num *= 2
        print(num)

lista_de_numeros = [2, 4, 5]

dobro(lista_de_numeros)
# %%
