# %%
# Exercício 1
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
soma = n1 + n2
print(f'A soma entre {n1} e {n2} é igual a: {soma}')
# %%
# Exercício 2
algo = input('Digite algo: ')
print(type(algo))
print(algo.isalnum())
print(algo.isalpha())
print(algo.islower())
print(algo.isupper())
print(algo.isnumeric())
print(algo.istitle())
print(algo.isidentifier())
# %%
# Exercício 3
n1 = int(input('Digite um número: '))
print('O antecessor de {} é {}, e seu sucessor é {}.'.format(n1, n1-1, n1+1))
# %%
# Exercício 4
n1 = int(input('Digite um número: '))
print('Número selecionado: {}\nDobro: {}\nTriplo: {}\nRaiz quadrada: {}'.format(n1, n1*2, n1*3, n1**(1/2)))
# %%
# Exercício 5
n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
print('A média do aluno é {}'.format((n1+n2)/2))
# %%
# Exercício 6
n1 = int(input('Digite um valor em metros: '))
print('{}m são {}cm'.format(n1, n1*100))
# %%
# Exercício 7
n1 = int(input('Digite um número: '))
for i in range(0, 11):
    print(f'{n1}x{i} = {n1*i}')
# %%
# Exercício 8
n1 = float(input('Digite um valor em R$: '))
print('R$ {} = USD {}'.format(n1, n1*3.27))
# %%
# Exercício 9
n1 = float(input('Digite a largura da parede em metros: '))
n2 = float(input('Digite a altura da parede em metros: '))
area = n1*n2
print('Para pintar uma parede com área de {}m² são necessários {} litros de tinta'.format(area, area/2))
# %%
# Exercício 10
n1 = float(input('Digite o valor de um produto: '))
print('O produto de valor {}, com 5% de desconto fica {}'.format(n1, n1-(n1*0.05)))
# %%
# Exercício 11
n1 = float(input('Digite o salário: '))
print('O seu salário com 15% de aumento ficará: {}'.format(n1+(n1*0.15)))
# %%
