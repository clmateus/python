# %%
# Consumo de API's
import requests

url = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'

response = requests.get(url)

if response.status_code == 200:
    print('Conexão bem-sucedida!')
    # print(response.json())

    dados = response.json()

    cotacao_dolar = dados['USDBRL']['bid']
    cotacao_euro = dados['EURBRL']['bid']
    cotacao_btc = dados['BTCBRL']['bid']

    print(f"Dólar: R$ {cotacao_dolar}")
    print(f"Euro: R$ {cotacao_euro}")
    print(f"Bitcoin: R$ {cotacao_btc}")
else:
    print('Erro na conexão:', response.status_code) 
# %%
