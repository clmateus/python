# %%
import requests
from bs4 import BeautifulSoup

# 1. Definir o alvo
url = "http://quotes.toscrape.com"

# 2. Fazer o pedido
response = requests.get(url)

# 3. Verificar se funcionou (Código 200 = OK)
print(f"Status da conexão: {response.status_code}")

# 4. HTML inteiro
# print(response.text)

# 5. BeautifulSoup
site = BeautifulSoup(response.text, 'html.parser')

# 6. Encontrar o primeiro elemento que coincide
frase = site.find("span", class_="text")

# 7. Mostrar apenas o texto sem as tags HTML
print(f'A frase do dia é:')
print(frase.get_text())
# %%
# 8. Extrair TODOS os elementos da página
citacoes = site.find_all("div", class_="quote")

print(f'--- TODAS AS CITAÇÕES DA PÁGINA ---')

for item in citacoes:
    texto = item.find("span", class_="text").get_text()
    autor = item.find("small", class_="author").get_text()
    
    print(f"Frase: {texto}")
    print(f"Autor: {autor}")
    print("-" * 30)
