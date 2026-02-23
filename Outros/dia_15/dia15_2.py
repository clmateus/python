# %%
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By   # Para encontrar elementos
from selenium.webdriver.common.keys import Keys # Para apertar Enter
import time

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get("https://www.google.com")

# 1. Encontrar a barra de pesquisa
# (No Google, o 'name' da barra de pesquisa é sempre 'q')
campo_busca = navegador.find_element(By.NAME, "q")

# 2. Escrever algo
campo_busca.send_keys("Cotação Dólar Hoje")

# 3. Apertar ENTER
campo_busca.send_keys(Keys.ENTER)

print("Pesquisa feita! Veja o resultado.")
input("Pressione ENTER no terminal para fechar...") # O programa espera você autorizar
navegador.quit()
# %%
