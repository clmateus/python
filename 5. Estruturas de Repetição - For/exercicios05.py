# %%
# Exercício 1
numero = int(input("Quer a tabuada de qual número? "))

print(f"Tabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
# %%
# Exercício 2
lista = ['Python', 'SQL', 'Git', 'Excel', 'PowerBI']

for item in lista:
    print(f'Aprendendo: {item}')
# %%
# Exercício 3
lista = []
soma = 0

for i in range(0, 5):
    preco_produto = float(input(f'Digite o valor do produto {i + 1}: '))
    lista.append(preco_produto)
    soma += preco_produto

print(f'O total deu: R$ {soma}')
# %%
