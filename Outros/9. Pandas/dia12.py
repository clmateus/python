# %%
# Pandas
with open("vendas.csv", "w", encoding='utf-8') as f:
    f.write("Data,Produto,Quantidade,ValorUnitario\n")
    f.write("01/01/2025,Notebook,5,3500.00\n")
    f.write("02/01/2025,Mouse,10,50.00\n")
    f.write("03/01/2025,Teclado,8,120.00\n")
    f.write("04/01/2025,Monitor,3,1200.00\n")
    f.write("05/01/2025,Notebook,2,3500.00\n")
print("Ficheiro vendas.csv criado com sucesso!")
# %%
import pandas as pd

# 1. Carregar a base de dados
tabela = pd.read_csv('vendas.csv')

# 2. Visualizar as primeiras 5 linhas
print('--- Primeiras Linhas ---')
print(tabela.head(), '\n')

# 3. Ver informações técnicas (tipos de dados e se há valores vazios)
print('--- Informações da Tabela ---')
print(tabela.info(), '\n')

# 4. Ver estatísticas (média, desvio padrão, min, max, etc.)
print('--- Resumo Estatístico ---')
print(tabela.describe(), '\n')

# 5. Manipulação de colunas
tabela['Faturamento'] = tabela['Quantidade'] * tabela['ValorUnitario']

print('--- Tabela com Faturamento ---')
print(tabela)

total_vendas = tabela['Faturamento'].sum()
print(f'O faturamento total da loja foi: R$ {total_vendas:.2f}')
# %%
