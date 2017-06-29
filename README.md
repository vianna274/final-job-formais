# MotivApp - Trabalho Final Formais

MotivApp é um aplicativo motivacional criado para o trabalho final da cadeira Linguagens Formais e Autômatos do institudo de informática - UFRGS.

## Como utilizar

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Pré-requesitos 

Para utilizar o aplicativo com a aplicação em python é necessário o .web module do python 2.7.x, pois o 3.x.x não estabilizou ainda.

```
Basta executar o arquivo em Python que ele lhe dirá qual module estará faltando.
```

### Instalando

Basta clonar o diretório, ou baixar manualmente e executar o arquivo .py desejado.
Para ser possível a execução será necessário a modificação de alguns arquivos para abstrair a parte de webservice utilizada pelo aplicativo.


## Testando

Há 2 arquivos que podem ser testados:
# Parser
Para testar basta implementar um hardcoded da sua gramática dentro do algoritmo e a frase que será reconhecida pelo parser. Ele retornará se foi, ou não reconhecida.
# Generator
Este necessita apenas da gramática hardcoded e a partir disso toda vez que for executado


## Lançamento

Dia XX/07/2017 durante a aula de Linguagens Formais e Autômatos

## Autores

* **Leonardo Vianna** - *Python Developer* - [PurpleBooth](https://github.com/vianna274)

* **Andy Ruiz Garramones** - *Python Developer* - [PurpleBooth](https://github.com/Andy9822)

* **João Vitor de Camargo** - *Android Developer* - [PurpleBooth](https://github.com/jvdecamargo)

* **Marlize Ramos** - *Grammar Creator* - [PurpleBooth](https://github.com/lizerb)

* **Matheus Rhoden** - *Support* - [PurpleBooth](https://github.com/matheusrhoden)


# trabFinalFormais
Trabalho final da cadeira Linguagens formais - Gerador de Linguagens

formais.py = Arquivo gerador de frases a partir de uma gramática previamente dada no texto "sample.txt" (Não utiliza Early)

input.py = Arquivo leitor do sample.txt

parser.py = Arquivo reconhecedor de uma frase a partir de uma gramática previamente dada no texto "sample.txt"

*Class.py = Classes que são importadas nos outros arquivos

generator.py = Arquivo gerador de frases a partir de uma gramática previamente dada (Utiliza Early)

*.apk = Aplicativo pronto
