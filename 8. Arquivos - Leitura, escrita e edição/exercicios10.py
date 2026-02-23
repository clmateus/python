# %%
# Exercício 1
with open('tarefas.txt', 'w', encoding='utf-8') as arquivo:
    for i in range(1, 5):
        tarefa = str(input(f'Digite a tarefa n°{i}'))
        arquivo.write(f'{tarefa}\n')
    print('Tarefas guardadas com sucesso!')
# %%
# Exercício 2
try:
    with open('tarefas.txt', 'r', encoding='utf-8') as f:
        contador = 0
        for linha in f:
                contador += 1
                print(f'Tarefa n°{contador}: {linha.rstrip()}')
except FileNotFoundError:
     print('ERRO: ARQUIVO NÃO ENCONTRADO.')
# %%
# Exercício 3
from random import randint

numero_aleatorio = randint(1, 10)
print(f'Pensei em um número entre 1 e 10!')
numero_usuario = int(input(f'Tente adivinhar! Digite aqui seu palpite: '))

with open('historico.txt', 'a', encoding='utf-8') as f:
    if numero_aleatorio == numero_usuario:
         f.write(f'Vitória - Jogador escolheu {numero_usuario} e Computador {numero_aleatorio}\n')
    else:
         f.write(f'Derrota - Jogador escolheu {numero_usuario} e Computador {numero_aleatorio}\n')     
# %%
