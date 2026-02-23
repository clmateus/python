# %%
with open(file='arquivo.txt', mode='w', encoding='utf-8') as fp:
    linha = 'arquivo txt' + '\n'
    fp.write(linha)

# %%
with open(file='arquivo.txt', mode='r', encoding='utf-8') as leitura:
    with open(file='arquivo.csv', mode='w', encoding='utf-8') as escrita:
        linha = leitura.readline()
        
        while linha:
            escrita.write(linha)
            linha = leitura.readline()
# %%
