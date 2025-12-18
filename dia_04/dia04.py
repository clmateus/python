# %%
# Listas e seus métodos
# Criação da lista
numeros = [2, 5, 9, 1]
print(numeros, 'Lista criada')

# Modificação de um valor da lista
numeros[2] = 3
print(numeros[2], 'Modificado o índice 2')

# Inserção de um novo valor na lista
numeros.append(7)
print(numeros, 'Método append()')

# Inserção de valor em posição específica
numeros.insert(2, 0)
print(numeros, 'Método insert()')

# Remoção de um valor da lista
numeros.pop(2)
print(numeros, 'Método pop()')

# Remoção da primeira ocorrência de um valor específico
numeros.remove(2)
print(numeros, 'Método remove()')

# Reordenar os valores em ordem crescente
numeros.sort()
print(numeros, 'Método sort()')

# Reordenar os valores em ordem decrescente
numeros.sort(reverse=True)
print(numeros, 'Método sort(reverse=True)')

# Quantidade de valores de uma lista
print(f'Essa lista tem {len(numeros)} itens.')
# %%
# Remoção condicional
if 4 in numeros:
    numeros.remove(4)
    print(f'Número 4 removido da lista.')
else:
    print(f'A lista não possui o número 4.')
# %%
# Percorrer listas com laços de repetição
for chave, valor in enumerate(numeros):
    print(f'Índice {chave}: {valor}')
# %%
# Criar listas com laço de repetição
valores = list()
for c in range(0, 5):
    valores.append(int(input('Digite um número inteiro: ')))
print(valores)
# %%
# Listas interligadas
lista1 = [1, 2, 3]
lista2 = lista1
lista2.pop()
print(lista1, lista2)
# %%
# Listas independentes
lista1 = [1, 2, 3]
lista2 = lista1[:]
lista2.pop()
print(lista1, lista2)
# %%
