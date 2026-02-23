# %%
idades = [25, 23, 28, 26]
# %%
# Write
with open(file='./idades.csv', mode='w', encoding='utf-8') as fp:
    linha = 'idade' + '\n' # Cabeçalho
    fp.write(linha)

    for idade in idades:
        linha = str(idade) + '\n'
        fp.write(linha) 
# %%
# Append
with open(file='./idades.csv', mode='a', encoding='utf-8') as fp:
    for idade in idades:
        linha = str(idade + 100) + '\n'
        fp.write(linha)
# %%
