# Programação Funcional

A programação funcional é um dos 3 paradigmas de programação:
1. Programação imperativa
2. Programação funcional
3. Programação orientada a objetos

Podemos entender um paradigma de programação como se fosse um estilo único de desenvolver códigos.

O Python é uma linguagem multi-paradigma, ou seja, ele não obriga o programador a usar um estilo único de codificação, permitindo até mesmo combinar essas abordagens no mesmo projeto para resolver problemas da maneira mais simples ou eficiente.

A programação funcional é o estilo que busca manipular dados com muitas e pequenas funções.

## Função Lambda

Função lambda ou função anônima é uma função que receberia um bloco de código muito enxuto e que pode ser salvo em uma variável. Em geral é utilizada com outros métodos funcionais como o map, filter e reduce.

Veja a estrutura de uma função lambda:
```
variavel = lambda params: expressão
```

### Função de alta ordem

Muito utilizadas junto das funções lambda, funções de alta ordem são aquelas que recebem outras funções como parâmetro ou que retornam outra função.

Veja um exemplo:
```
def retorno(juros: float):
    return lambda investimento: investimento * (1 + juros)
```

## Função map

A função map permite executar uma função a todos os elementos de uma coleção (listas, dicionários, etc.) e retornar todos os elementos transformados.

Veja a estrutura da função map:
```
variavel = map(função, coleção)
```

Exemplo de uso:
```
numeros = [1, 2, 3]

numeros_ao_cubo = map(lambda num: num ** 3, numeros)
```

Uma grande vantagem da função map é que ela mantém os dados pré-processados mas não os executa imediatamente. Por exemplo, na situação acima a variável "numeros_ao_cubo" não está contendo a lista de números elevados, mas um "map object" que só será de fato transformado em lista quando solicitado. Essa forma de operação permite que a aplicação se torne mais leve e rápida, evitando o consumo desnecessário de memória.

Outra vantagem da função map é que o Python executa as operações em cada item da coleção de maneira paralela, ou seja, em vez de iterar de um em um, todos os itens são operados ao mesmo tempo. Isso resulta em aplicações extremamente mais rápidas que as feitas segundo a programação imperativa.

## Função filter
