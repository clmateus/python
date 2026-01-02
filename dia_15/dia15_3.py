# %%
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By   # Para encontrar elementos
from selenium.webdriver.common.keys import Keys # Para apertar Enter
import time

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get("https://www.saucedemo.com/")

# 1. Preencher Usuário (standard_user é um usuário de teste desse site)
navegador.find_element(By.ID, "user-name").send_keys("standard_user")

# 2. Preencher Senha
navegador.find_element(By.ID, "password").send_keys("secret_sauce")

# 3. Clicar no botão Login
navegador.find_element(By.ID, "login-button").click()

print("Login realizado com sucesso!")
input("Pressione Enter para sair...")
navegador.quit()
# %%
