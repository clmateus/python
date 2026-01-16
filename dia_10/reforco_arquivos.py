# %%
# Leitura de todo o conteúdo de um arquivo
with open(file='./banco.csv', mode='r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()

print(conteudo)
# %%
# Leitura de um arquivo uma linha por vez
conteudo = []

with open(file='./banco.csv', mode='r', encoding='utf-8') as f:
    linha = f.readline() # Lê a primeira linha. O Python sabe que uma linha chegou ao fim quando encontra um \n
    while linha:
        conteudo.append(linha)
        linha = f.readline() # Lê uma nova linha, se a linha não existir, salva o valor None

for linha in conteudo:
    print(linha)
# %%
