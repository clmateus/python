# %%
# Pandas
with open("./vendas.csv", "w", encoding='utf-8') as f:
    f.write("Data,Produto,Quantidade,ValorUnitario\n")
    f.write("01/01/2025,Notebook,5,3500.00\n")
    f.write("02/01/2025,Mouse,10,50.00\n")
    f.write("03/01/2025,Teclado,8,120.00\n")
    f.write("04/01/2025,Monitor,3,1200.00\n")
    f.write("05/01/2025,Notebook,2,3500.00\n")
    f.write("05/01/2025,Notebook,2,3500.00\n")
    f.write("05/01/2025,Notebook,2,3500.00\n")
print("Ficheiro vendas.csv criado com sucesso!")
# %%
import pandas as pd

tabela = pd.read_csv('vendas.csv')

tabela['Faturamento'] = tabela['Quantidade'] * tabela['ValorUnitario']

print('--- Vendas de Notebook ---')

vendas_notebook = tabela[tabela['Produto'] == 'Notebook']
print(vendas_notebook, '\n')

print('--- Vendas Altas (Acida de R$ 2000,00) ---')

vendas_altas = tabela[tabela['Faturamento'] >= 2000]
print(vendas_altas, '\n')

print('--- Faturamento por Produto ---')

por_produto = tabela.groupby('Produto').sum(numeric_only=True)

print(por_produto[['Faturamento']], '\n')

print('--- Mais de 3 notebooks vendidos ---')

mais_de_tres_notebooks = tabela[(tabela['Produto'] == 'Notebook') & (tabela['Quantidade'] > 3)]
print(mais_de_tres_notebooks, '\n')
# %%