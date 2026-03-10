# %%
# wget - módulo que serve para fazer download de arquivos através de URLs
import wget
# zipfile - módulo nativo do python que serve para descompactar arquivos
import zipfile
# os - módulo nativo do python que serve para fazer operações com o sistema operacional
import os
# pandas - pacote que serve para manipulação de dados
import pandas as pd

if os.path.exists('./dados.zip'):
   os.remove('./dados.zip')

wget.download(url='https://archive.ics.uci.edu/ml/machine-learning-databases/00312/dow_jones_index.zip', out='./dados.zip')

with zipfile.ZipFile('./dados.zip', 'r') as fp:
    fp.extractall('./dados')

os.rename('./dados/dow_jones_index.data', './dados/dow_jones_index.csv')

# df = dataframe, uma estrutura de dados com métodos e atributos para processamento de dados
df = pd.read_csv('./dados/dow_jones_index.csv')
# %%
# Visualização das 10 primeiras linhas do arquivo
# df.head(n=10)

# # Visualização do nome das colunas
# df.columns.to_list()

# # Verificação do número de linhas e colunas
# linhas, colunas = df.shape
# print(f'Número de linhas: {linhas}')
# print(F'Número de colunas: {colunas}')
# %%
# Extraindo dados específicos das ações do McDonalds
df_mcd = df[df['stock'] == 'MCD']

df_mcd = df_mcd[['date', 'open', 'high', 'low', 'close']]

for col in ['open', 'high', 'low', 'close']:
  df_mcd[col] = df_mcd[col].apply(lambda value: float(value.split(sep='$')[-1]))

print(df_mcd)
# %%
