# %%
# Tipos primitivos
# Int (números inteiros) = 5, 6, 0, -4, 2132, -5421
# Float (números reais/ponto flutuante) = 5.0, 6.5, 0.321, -5.32
# Bool (booleanos) = True, False
# Str (strings) = 'aaa', 'um texto', ''
print(type(5))
print(type(5.0))
print(type(True))
print(type(''))
# %%
# Método format()
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
soma = n1 + n2
print('A soma entre {} e {} é igual a {}'.format(n1, n2, soma))
# %%
# Operações Aritméticas
# Adição = +
# Subtração = -
# Multiplicação = *
# Divisão = /
# Potência = ** ou método pow()
# Divisão inteira = //
# Sobra da divisão = %
print(5+2)
print(5-2)
print(5*2)
print(5/2)
print(5**2)
print(pow(5,2))
print(5//2)
print(5%2)
# %%
# Ordem de precedência
# 1 - Operações entre parênteses - ()
# 2 - Exponenciação - **
# 3 - Operações de multiplicação, divisão, divisão inteira e resto de divisão na ordem que aparecerem - *, /, //, %
# 4 - Soma e subtração - +, - 
print(5+3*2)
print(3*5+4**2)
print(3*(5+4)**2)
# %%
# Raiz quadrada e raiz cúbica
print(81**(1/2))
print(127**(1/3))
# %%
# Multiplicação de strings
print('Oi'*10)
# %%
# Mais formas de formatação
nome = input('Digite o seu nome: ')
print('Prazer em te conhecer {}!'.format(nome))
print('Prazer em te conhecer {:20}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))
# %%