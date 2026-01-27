# %%
# Função lambda simples
extrair_provedor_email = lambda email: email.split(sep='@')[-1]

email = 'cl.mateuscosta@gmail.com'
provedor_email = extrair_provedor_email(email)
print(provedor_email)
# %%
# Função lambda com estrutura condicional
numero_e_par = lambda numero: True if numero % 2 == 0 else False

for numero in range(1, 11):
    print(f'{numero} é par? {numero_e_par(numero)}')
# %%
# Função de alta ordem