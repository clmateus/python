# %%
# Comando import
import random
import math
# %%
# Uso de métodos personalizados dos módulos importados
print(random.choice([1, 2, 3]))
print(random.random())
print(math.pow(10, 2))
print(math.ceil(10.1))
print(math.floor(10.9))
# %%
# Importando um ou mais métodos específicos de um módulo sem importá-lo inteiro
from time import time, sleep

print(time())
print(sleep(1))
# %%
# Apelidando um módulo
from datetime import datetime as dt

print(dt.now())
print(dt.now().day)
print(dt.now().year)
# %%
