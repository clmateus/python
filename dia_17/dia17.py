# %%
import requests
import pandas as pd
from datetime import datetime
import os

def pegar_cotacoes():
    # 1. Extrair dados da API
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
    response = requests.get(url)
    
    if response.status_code == 200:
        json_data = response.json()
        return json_data
    else:
        print("Erro ao conectar na API")
        return None

def gerar_excel(dados_brutos):
    # 2. Organizar os dados
    
    # Pegando data e hora atual formatada (Dia/Mês/Ano Hora:Minuto)
    data_atual = datetime.now().strftime('%d/%m/%Y %H:%M')
    
    # Criando uma lista de dicionários para facilitar a criação da tabela
    lista_cotacoes = [
        {
            "Moeda": "Dólar (USD)",
            "Cotação": float(dados_brutos['USDBRL']['bid']),
            "Data Coleta": data_atual
        },
        {
            "Moeda": "Euro (EUR)",
            "Cotação": float(dados_brutos['EURBRL']['bid']),
            "Data Coleta": data_atual
        },
        {
            "Moeda": "Bitcoin (BTC)",
            "Cotação": float(dados_brutos['BTCBRL']['bid']),
            "Data Coleta": data_atual
        }
    ]
    
    # Criar o DataFrame (Tabela do Pandas)
    tabela = pd.DataFrame(lista_cotacoes)
    
    print("--- Prévia do Relatório ---")
    print(tabela)
    
    # 3. Salvar em XLSX
    nome_arquivo = "Relatorio_Financeiro.xlsx"
    tabela.to_excel(nome_arquivo, index=False) # index=False tira a coluna de números 0,1,2
    
    print(f"\nSucesso! O arquivo '{nome_arquivo}' foi gerado na pasta.")

# --- Execução Principal ---
print("Iniciando o Bot Financeiro...")
dados = pegar_cotacoes()

if dados:
    gerar_excel(dados)
else:
    print("Não foi possível gerar o relatório.")
# %%
