# %%
# Exercício 1
lista = list()
for i in range(0, 5):
    lista.append(float(input('Digite um valor: ')))
print(f'Maior valor inserido: {lista[1]}')
print(f'Menor valor inserido: {lista[1]}')
# %%
# Exercício 1
tarefas = ['Fazer café', 'Estudar', 'Trabalhar', 'Treinar']
print(tarefas)
print(tarefas[2])
tarefas[1] = 'Estudar Python'
print(tarefas)
# %%
# Exercício 2
jogadores = []

for i in range(0, 5):
    jogadores.append(str(input('Digite o nome de um jogador: ')))

print(f'A sua equipe tem os seguintes jogadores:', jogadores)
# %%
# Exercício 3
frutas = ['Maçã', 'Banana', 'Morango', 'Uva']
print(frutas)

frutaDetestavel = input('Digite qual dessas frutas você detesta: ')

if frutaDetestavel in frutas:
    frutas.remove(frutaDetestavel)
else:
    print('Fruta não encontrada.')

print(frutas)
# %%
