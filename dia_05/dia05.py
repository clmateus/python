# %%
# Estruturas de Repetição
numero = int(input("Quer a tabuada de qual número? "))

print(f"Tabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
# %%
