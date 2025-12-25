# %%
# Exercício 1
import math

numero_real = float(input('Digite um número real: '))
porcao_inteira = math.floor(numero_real)

print(f'A porção inteira de {numero_real} é {porcao_inteira}')
# %%
# Exercício 2
import math

cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

print(f'A hipotenusa do triângulo retângulo inserido é {hipotenusa}')
# %%
# Exercício 3
import math

angulo = float(input('Digite o valor de um ângulo qualquer: '))
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)

print(f'Ângulo: {angulo}')
print(f'Seno: {seno}')
print(f'Cosseno: {cosseno}')
print(f'Tangente: {tangente}')
# %%
# Exercício 4
import random

alunos = []

while True:
    aluno = str(input('Digite o nome do aluno: '))
    alunos.append(aluno)

    if len(alunos) == 4:
        break

aluno_sorteado = random.randint(0, 3)

print(f'Os seguintes alunos foram registrados: {alunos}')
print(f'O aluno que irá apagar o quadro será o: {alunos[aluno_sorteado]}')
# %%
# Exercício 5
import random

alunos = []

while True:
    aluno = str(input('Digite o nome do aluno: '))
    alunos.append(aluno)

    if len(alunos) == 4:
        break

random.shuffle(alunos)

print(f'A ordem de apresentação será: {alunos}')
# %%
# Exercício 6
import Play_mp3

Play_mp3.play(filename='./mp3.mp3')
# %%
