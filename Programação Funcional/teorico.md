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

A função filter aplica uma função lógica em todos os elementos de uma coleção e retorna apenas aqueles que resultam em verdadeiro. O retorno do filter é sempre um valor booleano.

Veja a estrutura da função filter:
```
variavel = filter(função, coleção)
```

Exemplo de uso:
```
numeros = [1, 2, 3]

numeros_impares = filter(lambda num: num % 2 != 0, numeros)
```

Assim como na função map, o filter também retém os dados sem executá-los imediatamente. Sendo assim, no exemplo acima a variável "numeros_impares" não possui a lista pronta, mas um "filter object".

## Função reduce

A função reduce tem como objetivo transformar uma coleção inteira em um único valor, aplicando uma função de forma cumulativa.

Diferente das outras, a função reduce não faz parte nativa do Python, sendo necessário importá-la através da biblioteca functools:
```
from functools import reduce
```

Veja a estrutura da função reduce:
```
variavel = reduce(função, coleção)
```

Exemplo de uso:
```
numeros = [1, 2 ,3]

soma = reduce(lambda x, y: x + y, numeros)
```

É importante observar que diferente das funções map e filter, a função reduce não mantém os dados em um objeto, ou seja, no exemplo acima a variável soma guarda realmente o valor "6".

## Compossibilidade

A compossibilidade é quando combinamos dois ou mais métodos funcionais.

Veja abaixo um exemplo onde os três métodos funcionais são usados:
```
numeros = [1, 2, 3, 4, 5, 6, 7]

soma_numeros = reduce(lambda x,y: x + y, filter(lambda numero: numero % 2 != 0, map(lambda numero: numero ** 2, numeros)))
```

Esse código está:
1. Elevando todos os números da lista ao quadrado usando o map
2. Selecionando apenas os números ímpares usando o filter
3. Somando todos os números, resultando em um único valor final usando o reduce 