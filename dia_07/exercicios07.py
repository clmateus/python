# %%
# Exercício 1
def area(largura, comprimento):
    area = largura * comprimento
    return f'A área de um terreno {largura}x{comprimento} é de {area}m².'

largura = float(input(f'Digite a largura do terreno em metros: '))
comprimento = float(input(f'Digite o comprimento do terreno em metros: '))

area(largura, comprimento)
# %%
# Exercício 2
def escreva(texto):
    print('-'*len(texto))
    print(f'{texto}')
    print('-'*len(texto))

escreva('Olá, mundo!')
# %%
# Exercício 3
def voto(idade):
    if idade < 18:
        return 'NEGADO'
    elif idade >= 18:
        return 'OPCIONAL'
    else: 
        return 'ERRO'

ano = int(input('Em que ano você nasceu?'))
idade = 2025 - ano

print(voto(idade))
# %%
