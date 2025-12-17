# %%
# Condições
# Estrutura condicional simples
nome = str(input('Qual é o seu nome?'))

if nome == 'José':
    print('Seu nome é José!')

print('Bom dia {}'.format(nome))
# %%
# Estrutura condicional composta
nome = str(input('Qual é o seu nome?'))

if nome == 'José':
    print('Seu nome é José!')
else:
    print('Seu nome não é José!')

print('Bom dia {}'.format(nome))