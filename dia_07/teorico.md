# Funções

Funções são estruturas que permitem reutilizar um bloco de código várias vezes.

Podemos criar e posteriormente chamar uma função no Python da seguinte maneira:
```
def nome_da_funcao(parametro1, parametro2, ...):
    bloco de código
    return valor_a_ser_retornado

nome_da_funcao('', '')
```

Os parâmetros das funções podem ter os seus tipos especificados:
```
def soma(num1, num2: int):
    return num1 + num2

def mensagem(texto: str):
    print(texto)

soma(1, 1)
mensagem('Bom dia!')
```

## Retorno

Toda função retorna algum valor. Se não for especificado, por padrão a função retornará o valor None.

O retorno, assim como os parâmetros, também pode ter o seu tipo especificado:
```
def texto_em_maiusculo(texto: str) -> str:
    texto_maiusculo = texto.upper()
    return texto_maiusculo

def numero_de_caracteres_em_uma_frase(texto: str) -> int:
    quantidade_de_caracteres = len(texto)
    return quantidade_de_caracteres
```

Podemos atribuir o retorno das funções a uma variável:
```
def funcao_com_retorno(n1, n2: int) -> int:
    return n1 + n2

def funcao_sem_retorno(n1, n2: int):
    print(n1 + n2)

resultado1 = funcao_com_retorno(1, 1) # 2
resultado2 = funcao_sem_retorno(1, 1) # None
```

As funções podem ter múltiplos retornos:
```
def extrair_usuario_email_provedor(email: str) -> (str, str):
    email_separado = email.split(sep='@')
    usuario = email_separado[0]
    provedor = email_separado[1]
    return usuario, provedor
```

## Parâmetros

Parâmetros são os valores passados na chamada da função. Eles não são obrigatórios:
```
    def funcao_sem_parametro() -> float:
        return 3.1415

    def funcao_com_parametros(parametro1, parametro 2: float) -> float:
        return parametro1 * parametro2