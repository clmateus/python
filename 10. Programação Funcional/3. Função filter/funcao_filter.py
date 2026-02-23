# %%
# Função filter
numeros = [1, 2, 3]

numeros_impares = filter(lambda num: num % 2 != 0, numeros)

print(list(numeros_impares))
# %%
# Função filter com alta ordem
emails = ['email1@gmail.com', 'email2@hotmail.com', 'email3@gov.br']

provedor_gmail = filter(lambda email: 'gmail' in email, emails)

print(list(provedor_gmail))
# %%
