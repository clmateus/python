# %%
# O for é utilizado para iterar sobre coleções (listas, tuplas, dicionários, conjuntos e strings) ou sobre qualquer iterável (como o range).
colecao = ['a', 'b', 'c',]

for a in colecao:
    print(a) # a, b, c
# %%
# Iterando sobre operador range
for valor in range(6):
    print(valor) # 0, 1, 2, 3, 4, 5
# %%
# Iterando sobre range com início e fim
soma = 0

for valor in range(0, 11):
    soma += valor

print(soma) # 55
# %%
# Iterando sobre range com passo
for valor in range(2, 11, 2):
    print(valor) # 2, 4, 6, 8
# %%
# Iterando sobre listas
frutas = ['laranja', 'maçã', 'banana']

for fruta in frutas:
    print(fruta) # laranja, maçã, banana
# %%
# Iterando sobre strings
for letra in 'Python':
    print(letra) # P, y, t, h, o, n

frase = 'Python é legal'
for letra in frase:
    print(letra) # P, y, t, h, o, n,  , é,  , l, e, g, a, l
for letra in frase:
    if (letra == 'y') | (letra == 'n'):
        print(f'A frase possui a letra {letra}')
# %%
# Iterando sobre dicionários
dicionario = {
    '123': '456',
    '789': '012',
    '345': '678'
}

# Iterando sobre a chave e o valor dos itens do dicionário
for chave, valor in dicionario.items():
    print(chave) # 123, 789, 345
    print(valor) # 456, 012, 678
    print(f'A chave {chave} tem o valor {valor} \n')

# Iterando apenas sobre as chaves do dicionário
for chave in dicionario.keys():
    print(f'Key: {chave}')

# Iterando apenas sobre os valores do dicionário
for valor in dicionario.values():
    print(f'Value: {valor}')
# %%
# Quebra de repetição
for i in range(0, 10*10*10*10*10*10):
    print(i)
    if i == 2:
        break

numeros = [1, 5, 9, 13, 14, 23, 20, 18]

for i in numeros:
    if (i % 2) == 0:
        print(f'O número {i} é par!\nFim do loop.')
        break
    else:
        print(f'O número {i} é impar!')
# %%
# Avanço para próxima repetição
for i in numeros:
    if (i % 2) == 0:
        print(f'O número {i} é par!\nFim do loop.')
        break
    else:
        continue # Passa para a próxima repetição, sem executar o que estiver abaixo
        print(f'O número {i} é impar!')
# %%
