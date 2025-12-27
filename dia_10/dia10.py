# %%
# Manipulação de arquivos .txt
with open('teste.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Olá mundo!\n')
# %%
# Leitura
with open('teste.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
# %%
# Leitura linha a linha
with open('teste.txt', 'r', encoding='utf-8') as arquivo:
    i = 0
    for linha in arquivo:
        i += 1
        print(f'{i} - {linha.rstrip()}')
# %%
# Salvando conteúdo em variável global
with open('teste.txt', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()

print(linhas)

for l in linhas:
    print(l.rstrip())
# %%
# Adição de conteúdo
with open('teste.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write('Conteúdo adicionado!\n')
# %%