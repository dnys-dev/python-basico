# Protocolo

exemplo usando o __add__

quando o objeto implente __add__ nos diz que ele é implementa o protocolo `Addible` (aditivel), 

Ex:

```python
numero = 65
numero + 1 # isto é uma sintaxe sugar

""" por de baixo do pano o python faz esta operação
numero.__add__(1) lebrando que __<nome>__ são privado, só o python acessa. """

```
neste caso é implementado pelo o protocolo numero.__add__

o metodo de comparação é __eq__

ex: numero == 0

# Tipos de dados

Todas as informações que usaremos durante a programação são representadas na memória do computador através de um tipo de dado, você também vai ouvir os termos `classe` ou `categoria` para se referir a mesma coisa.

Todos os objetos em Python são formados por essas 3 propriedades:

- valor "1000010" ou "B"
- tipo ou classe str, int, float, ...
- posição na memória o número retornado pela função id()

## Metodos 

class int = class para inteiror

```python
dir(int)
```

os metódos que não começa com __ são metodos público e pode ser chamado diretamente no objeto.