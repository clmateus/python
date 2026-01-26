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
# Extração de valores de uma coluna específica
idades = []

with open(file='./banco.csv', mode='r', encoding='utf-8') as f:
    linha = f.readline() # Lê o cabeçalho
    linha = f.readline() # Lê a primeira linha

    while linha:
        linha_separada = linha.split(sep=',') # Quebra a string nas vírgulas e salva os resultados em uma lista
        idade = linha_separada[0] # Seleciona o primeiro elemento da lista (neste caso é a coluna idade)
        # idade = int(idade) # Transforma o valor idade de string para integer
        idades.append(idade) # Salva o valor idade na lista de idades
        linha = f.readline() # Lê a próxima linha. Caso ela não exista, salva o valor "None" que por sua vez encerra o laço de repetição

print(idades)
# %%
