# %%
# wget - módulo que serve para fazer download de arquivos através de URLs
import wget
# zipfile - módulo nativo do python que serve para descompactar arquivos
import zipfile
# os - módulo nativo do python que serve para fazer operações com o sistema operacional
import os
# pandas - pacote que serve para manipulação de dados
import pandas as pd
# seaborn - pacote que serve para visualização de dados
import seaborn as sns

if os.path.exists('./dados.zip'):
   os.remove('./dados.zip')

wget.download(url='https://archive.ics.uci.edu/ml/machine-learning-databases/00312/dow_jones_index.zip', out='./dados.zip')

with zipfile.ZipFile('./dados.zip', 'r') as fp:
    fp.extractall('./dados')

if os.path.exists('./dados/dow_jones_index.csv'):
   os.remove('./dados/dow_jones_index.csv')

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
# Extraindo dados específicos das ações da Coca-Cola
df_cc = df[df['stock'] == 'KO']

df_cc = df_cc[['date', 'open', 'high', 'low', 'close']]

for col in ['open', 'high', 'low', 'close']:
  df_cc[col] = df_cc[col].apply(lambda value: float(value.split(sep='$')[-1]))

print(df_cc)
# %%
# Visualizando os dados do McDonalds
plot = sns.lineplot(x='date', y='open', data=df_mcd)
plot.tick_params(axis='x', labelrotation=45)

plot = sns.lineplot(x='date', y='value', hue='variable', data=pd.melt(df_mcd, ['date']))
plot.tick_params(axis='x', labelrotation=45) 

plot.figure.savefig('./mcd.png')
# %%
# Visualizando os dados da Coca-Cola
plot = sns.lineplot(x='date', y='open', data=df_cc)
plot.tick_params(axis='x', labelrotation=45)

plot = sns.lineplot(x='date', y='value', hue='variable', data=pd.melt(df_cc, ['date']))
plot.tick_params(axis='x', labelrotation=45) 

plot.figure.savefig('./cc.png')
# %%
