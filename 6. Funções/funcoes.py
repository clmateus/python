# %%
def imprime(mensagem: str):
    print(mensagem)

imprime('Olá mundo!')
# %%
def soma(num1, num2: int):
    return num1 + num2

soma(2, 5)
# %%
def escreve_arquivo_csv(nome: str, cabecalho: str, conteudos: list) -> bool: 
    try: 
        with open(file=nome, mode='w', encoding='utf8') as fp: 
            linha = cabecalho + '\n' 
            fp.write(linha) 
            for conteudo in conteudos: 
                linha = str(conteudo) + '\n' 
                fp.write(linha) 
    except Exception as exc: 
        print(exc) 
        return False 

    return True

nome = 'arquivo_csv.csv'
cabecalho = 'idade'
conteudos = [25, 23, 20, 27]

escreveu_com_sucesso = escreve_arquivo_csv(nome=nome, cabecalho=cabecalho, conteudos=conteudos)
print(escreveu_com_sucesso)
# %%
def juros_compostos_anual(valor_inicial: float, taxa_juros_anual: float, anos: int) -> float:
    valor_final = valor_inicial

    for ano in range(1, anos+1): 
        valor_final = valor_final * (1 + taxa_juros_anual) 
        valor_final = round(valor_final, 2)

    print(f'Para um valor inicial de R$ {valor_inicial} e uma taxa de juros anual de {taxa_juros_anual}, em {anos} anos você terá R$ {valor_final}') 
    
    return valor_final
 
valor_inicial, taxa_juros_anual, anos = 1000.00, 0.05, 10 
valor_final = juros_compostos_anual(valor_inicial=valor_inicial, taxa_juros_anual=taxa_juros_anual, anos=anos)

valor_inicial, taxa_juros_anual, anos = 1020.00, 0.03, 10 
valor_final = juros_compostos_anual(valor_inicial=valor_inicial, taxa_juros_anual=taxa_juros_anual, anos=anos)
# %%
