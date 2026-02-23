# %%
# Dicionários
filme = {
    'título': 'Matrix',
    'ano': 1999,
    'diretor': 'Wachowski'
}

print(filme['título'])
print(filme['ano'])
print(filme['diretor'])
# %%
# Adição de elementos
filme['genero'] = 'Ficção'

print(filme['genero'])
# %%
# Percorrendo dicionário com laço de repetição
for chave, valor in filme.items():
    print(f'O {chave} é {valor}')
# %%
