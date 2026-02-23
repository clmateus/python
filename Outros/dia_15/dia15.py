# %%
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 1. Instala e configura o Driver do Chrome automaticamente
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

# 2. Entrar no site
navegador.get("https://www.google.com")

# 3. Esperar um pouco para você ver o resultado
print("Abri o Google! Vou fechar em 5 segundos...")
time.sleep(5)

# 4. Fechar o navegador (MUITO IMPORTANTE para não travar o PC)
navegador.quit()
# %%
