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



