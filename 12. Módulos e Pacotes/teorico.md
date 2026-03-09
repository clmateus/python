# Módulos e Pacotes

Módulos e pacotes são, de forma simplificada, conjuntos de código já prontos que podem ser importados para dentro do nosso projeto a fim de resolver um ou mais problemas específicos.

Módulos são os arquivos python em si, aqueles com extensão ".py".

Pacotes são um conjunto de módulos reunidos e organizados em um diretório.

A principal vantagem de utilizar módulos e pacotes é a reutilização de código. 

Podemos encontrar uma lista com vários módulos e pacotes neste [link](https://docs.python.org/3.15/py-modindex.html).

## PyPI e PIP

O PyPI é o repositório oficial de pacotes Python. O PIP é a gerenciador de pacotes oficial para instalar pacotes Python armazenados no PyPI.

A sintaxe para se instalar um pacote do PyPI usando o PIP é a seguinte:
```
!pip install <pacote>==<versão>
```
Quando não especificada, o PIP sempre irá instalar a versão mais atual do pacote solicitado. Mas como boa prática, é recomendado sempre especificar a versão, por mais que o intuito seja usar a mais recente.
Exemplo:
```
!pip install requests==2.25.1
```
Para listar todos os pacotes instalados no seu repositório usa-se o seguinte comando:
```
!pip freeze
```
Para remover um pacote do seu repositório usa-se o seguinte comando:
```
!pip uninstall <pacote>
```