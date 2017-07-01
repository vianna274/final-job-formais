# MotivApp - Trabalho Final Formais

MotivApp � um aplicativo motivacional criado para o trabalho final da cadeira Linguagens Formais e Aut�matos do institudo de inform�tica - UFRGS.

### Explica��o 

Para utilizar o aplicativo basta baixar o .apk em um celular android, ou emulador e executar o aplicativo normalmente.
Ele funciona da seguinte forma: o generator.py est� rodando em um server e fica gerando frases para um site do "pythonanywhere", o aplicativo feito em androidstudio consulta esse site e coloca a frase na tela do aplicativo substituindo a palavra USERNAME pelo nome do usu�rio no aplicativo.


### Pr�-requisitos 

Para desenvolver o aplicativo com a aplica��o em python em android � necess�rio o .web module do python 2.7.x, pois o 3.x.x n�o estabilizou ainda.

```
Basta executar o arquivo em Python que ele lhe dir� qual module estar� faltando.
```
```
Caso queira somente desenvolver o algoritmo em python basta excluir todas as partes do webservice.
```

### Instalando

Basta clonar o diret�rio, ou baixar manualmente e executar o arquivo .py desejado.
Para ser poss�vel a execu��o ser� necess�rio a modifica��o de alguns arquivos para abstrair a parte de webservice utilizada pelo aplicativo.


## Testando

H� 2 arquivos que podem ser testados:
### Parser.py
Para testar basta implementar um hardcoded da sua gram�tica dentro do algoritmo e a frase que ser� reconhecida pelo parser. Ele retornar� se foi, ou n�o reconhecida.
### Generator.py
Este necessita apenas da gram�tica hardcoded e a partir disso toda vez que for executado


## Arquivos Explicados
```
generator.py = Arquivo gerador de frases a partir de uma gram�tica previamente dada (Utiliza Early)

formais.py = Arquivo gerador de frases a partir de uma gram�tica previamente dada no texto "sample.txt" (N�o utiliza Early)

input.py = Arquivo leitor do sample.txt

parser.py = Arquivo reconhecedor de uma frase a partir de uma gram�tica previamente dada no texto "sample.txt"

*Class.py = Classes que s�o importadas nos outros arquivos

*.apk = Aplicativo pronto

sample.txt = Arquivo input com o formato correto para testes � necess�rio ser desse formato.
```

## Lan�amento

Dia XX/07/2017 durante a aula de Linguagens Formais e Aut�matos

## Autores

* **Leonardo Vianna** - *Python Developer* - (https://github.com/vianna274)

* **Andy Ruiz Garramones** - *Python Developer* - (https://github.com/Andy9822)

* **Jo�o Vitor de Camargo** - *Android Developer* - (https://github.com/jvdecamargo)

* **Marlize Ramos** - *Grammar Creator* - (https://github.com/lizerb)

* **Matheus Rhoden** - *Support* - (https://github.com/matheusrhoden)