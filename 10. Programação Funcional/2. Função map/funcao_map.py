# %%
# Função map
numeros = [1, 2, 3]

numeros_ao_cubo = map(lambda num: num ** 3, numeros)

print(list(numeros_ao_cubo))
# %%
# Função map com alta ordem
emails = ['email1@gmail.com', 'email2@hotmail.com', 'email3@gov.br']

provedores = map(lambda email: email.split(sep='@')[-1], emails)

print(list(provedores))
# %%
