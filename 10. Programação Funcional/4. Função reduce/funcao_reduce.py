# %%
# Importação
from functools import reduce
# %%
# Função reduce
numeros = [1, 2 ,3]

soma = reduce(lambda x, y: x + y, numeros)

print(soma)
# %%
# Função reduce com alta ordem
numeros = [50, 32, 92, 13]

maior_numero = reduce(lambda x, y: x if x >= y else y, numeros)

print(maior_numero)
# %%
# Compossibilidade
numeros = [1, 2, 3, 4, 5, 6, 7]

soma_numeros = reduce(lambda x,y: x + y, filter(lambda numero: numero % 2 != 0, map(lambda numero: numero ** 2, numeros)))

print(soma_numeros)
# %%
