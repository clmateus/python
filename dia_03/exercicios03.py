# %%
# Exercício 1
import random

n1 = random.randint(0, 5)
n2 = int(input('Eu pensei em um número entre 0 e 5. Tente adivinhar: '))

if n1 == n2:
    print('Você acertou, parabéns!')
else:
    print('Você errou, que pena!\nNúmero escolhido: {}\nNúmero sorteado: {}'.format(n2, n1))
# %%
# Exercício 2
n1 = int(input('Digite a velocidade do veículo: '))

if n1 > 80:
    print(f'Você foi multado! A multa custará R${(n1 - 80) * 7},00')
else:
    print('Velocidade permitida.')
# %%
# Exercício 3
n1 = int(input('Digite um número inteiro: '))

if n1 % 2 == 0:
    print(f'O número {n1} é par.')
else:
    print(f'O número {n1} é impar.')
# %%
# Exercício 4
n1 = float(input('Digite uma distância em KM: '))

if n1 <= 200:
    print(f'A viagem custará R${n1*0.50}')
else:
    print(f'A viagem custará R${n1*0.45}')
# %%
# Exercício 5
n1 = int(input('Digite um ano: '))

if n1 % 4 == 0:
    print('Ano bissexto.')
else:
    print('Ano comum.')
# %%
# Exercício 6
n1 = int(input('Digite o número 1: '))
n2 = int(input('Digite o número 2: '))
n3 = int(input('Digite o número 3: '))

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print(f'O maior número é o {maior} e o menor é o {menor}')
# %%
# Exercício 7
n1 = float(input('Digite o seu salário: '))

if n1 > 1250.00:
    print(f'Seu novo salário terá um aumento de 10%.\nNovo salário R${n1 + (n1*0.1)}')
else:
    print(f'Seu novo salário terá um aumento de 15%.\nNovo salário R${n1 + (n1*0.15)}')
# %%
# Exercício 8
n1 = float(input('Digite o comprimento da reta 1: '))
n2 = float(input('Digite o comprimento da reta 2: '))
n3 = float(input('Digite o comprimento da reta 3: '))

if ((n1 + n2) > n3) and ((n1 + n3) > n2) and ((n2 + n3) > n1):
    print('Essas retas podem formar um triângulo.')
else:
    print('Essas retas não podem formar um triângulo.')
# %%
