print(f'Boas vindas a calculadora de IMC!')

while True:
    try:
        print(f'Precisamos das suas medidas: ')
        peso = float(input('Digite o seu peso (KG): [Ex: 75.5]'))
        altura = float(input('Digite a sua altura (m): [Ex: 1.70]'))
        imc = peso / (altura * altura)
        diagnostico = ''

        if imc < 18.5:
            diagnostico = 'abaixo do peso'
        elif imc > 18.5 and imc < 24.9:
            diagnostico = 'peso ideal'
        elif imc > 25 and imc < 29.9:
            diagnostico = 'sobrepeso'
        else:
            diagnostico = 'obesidade'

        print(f'IMC calculado! Veja abaixo os seus resultados: ')
        print(f'Seu IMC: {imc}. Isso é considerado {diagnostico}.')
    
    except ValueError:
        print(f'ERRO: Por favor, digite apenas números (use pontos para decimais).')

    sair = input(f'Você deseja calcular novamente? (S/N)')

    if sair == 'N' or sair == 'n':
        break