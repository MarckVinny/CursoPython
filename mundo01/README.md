# :::::: Curso de Python ::::::
###### Ministrado pelo Professor Gustavo Guanabara do [Curso em Vídeo.](https://www.youtube.com/watch?v=S9uPNppGsGo&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=1)
---

## :::::::: Módulo 01 - Mundo 01 ::::::::

Na quarta aula foi criado um desafio *(Desafio 03)* para ler dois números e calcular a soma entre eles. 
No arquivo `exec003.py` dentro da pasta `/desafios`, se encontra tanto o desafio quanto a resposta.
Então foi feito da seguinte forma:
* Será aberto um `input` abrindo e fechando parenteses `()` e dentro será colocado uma mensagem e a mesma deve estar entre aspas simples para ***strings*** `''`.

* Com esse comando, `input('Digite um número')` tudo que for digitado será enviado para algum lugar, então, será criado uma ***variável*** *(lembrando que é um espaço na memória do dispositivo)* para guardar o que digitado.

* Então, a variável `n1` irá receber `=` *(1 sinal de igual lê-se: **recebe**)* o `input`, todo esse procedimento será repetido para a segunda variável `n2`.

* Agora iremos pegar os valore de `n1` e `n2` e somar que será colocado dentro de outra ***variável*** chamada `s`. Então, ficará assim: `s = n1 + n2` que lê-se, **s** recebe **n1** mais **n2**.

* O proximo passo é mostrar na tela a soma das duas variáveis, e para isso, iremos utilizar a Função `print()`, esse print mostrará duas coisas, uma string contendo a mensagem `'A soma vale:'` e a variável `s` contendo o resultado da soma, mas, para que isso ocorra, entre a string e a variável precisa ser separado por uma vírgula `,`.

* Que ficará da seguinte forma: `print('A soma vale: ', s)`.

Tudo isso, foi o *Desafio 03* que foi visto na *Aula 04*, mas, o código da forma que está, não irá funcionar corretamente.
Pois, o invés de fazer a soma de `n1 + n2`, ele irá concatenar *(juntar)*, pois, o sinal de + não estava servindo como adição, mas sim como concatenação e isso aconteceu porquê não foram usados os conceitos desta aula, que serão, os Tipos Primitivos.

## ::: Tipos Primitivos :::

Para resolver o problema, de que, quando o valor é digitado `input`, mesmo que seja um número, ele não é considerado como número, mas sim como sendo uma string.

Para resolver esse problema, será utilizado um Tipo Primitivo que no caso é o `int`.

```
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
s = n1 + n2

print('A soma vale: ', s)
```

Com isso, tudo que estiver entre os parênteses do `int()`, será convertido para um número inteiro.

```
int(input('Digite um número: '))
```
Com isso, o que está acontecendo é que: quando for digitado um valor, ele será jogado para dentro de `n1` como um número inteiro.

E no Python, não existe somente o ***Tipo Primitivo*** `int()` ***inteiro*** os 4 Tipos mais básicos veremos logo a seguir:

* ***Tipo int():*** Números inteiros, positivos, negativos e nulos.  
Ex.: `0`, `4`, `-7`, `9875`, etc.

* ***Tipo float():*** Números Reais ou números de Ponto Flutuante, positivos, negativos e nulos, mas, separados por um ponto `.`.  
Ex.: `0.0`, `0.075`, `4.5`, `7.0`, `-15.223`, etc.

* ***Tipo bool:*** Valores lógicos ou booleanos que são `True` verdadeiro e `False` falso.  
***ATENÇÃO:*** quando for usar valores booleanos, a primeira letra ***precisa ser maiúscula***.

* ***Tipo str:*** Valores caracteres ou string. Palavras escritas entre aspas simples `''`.  
Ex: `'Olá!'`, `'7.5'` e/ou `''` string vazia.

Outra forma de se usar os Tipos Primitivos no `print()`:

```
print('A soma vale', s)
```

Abaixo, terá a mesma funcionalidade, mas, com mais recursos.  
A diferença é que dentro da string agora tem um `par de chaves`, e essa máscara será substituída por um Método da própria string.  
Depois das aspas, será acrescentado o Método `.format()` e dentro dos parênteses do Método, será colocado o que será substituído pelo Método.  
Que em nosso exemplo será a variável `s`.

```
print('A soma vale{}'.format(s))
```

Aparentemente pode parecer que o código ficou maior que o anterior, mas, adiante ficará claro que não.

> ***DICA:** esta é a nova sintaxe usada no **Python3** e que será implementada em todo o decorrer do curso.  
**DICA":** para saber qual o Tipo Primitivo de cada variável, se usa o comando: `print(type(nome_variável))`*



