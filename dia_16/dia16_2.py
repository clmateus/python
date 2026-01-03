# %%
import requests

print("--- CONVERSOR EM TEMPO REAL ---")
reais = float(input("Quantos Reais (R$) você tem? "))

# Pegar cotação
url = "https://economia.awesomeapi.com.br/last/USD-BRL"
req = requests.get(url)
dados = req.json()

# O valor vem como string ("5.20"), precisamos converter para float
valor_dolar = float(dados['USDBRL']['bid'])

# Conta matemática
dolares_possiveis = reais / valor_dolar

print(f"\nCotação atual: US$ 1.00 = R$ {valor_dolar:.2f}")
print(f"Com R$ {reais:.2f} você consegue comprar US$ {dolares_possiveis:.2f}")
# %%
