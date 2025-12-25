# %%
# Exercício 1
aluno = {}
aluno["nome"] = input("Nome do aluno: ")
aluno["media"] = float(input(f"Média de {aluno['nome']}: "))

if aluno["media"] >= 7:
    aluno["situacao"] = "Aprovado"
else:
    aluno["situacao"] = "Reprovado"

print("-" * 30)
for k, v in aluno.items():
    print(f"  - {k} é igual a {v}")
# %%