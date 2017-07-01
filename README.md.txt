# MotivApp - Trabalho Final Formais

MotivApp é um aplicativo motivacional criado para o trabalho final da cadeira Linguagens Formais e Autômatos do institudo de informática - UFRGS.

### Explicação 

Para utilizar o aplicativo basta baixar o .apk em um celular android, ou emulador e executar o aplicativo normalmente.
Ele funciona da seguinte forma: o generator.py está rodando em um server e fica gerando frases para um site do "pythonanywhere", o aplicativo feito em androidstudio consulta esse site e coloca a frase na tela do aplicativo substituindo a palavra USERNAME pelo nome do usuário no aplicativo.


### Pré-requisitos 

Para desenvolver o aplicativo com a aplicação em python em android é necessário o .web module do python 2.7.x, pois o 3.x.x não estabilizou ainda.

```
Basta executar o arquivo em Python que ele lhe dirá qual module estará faltando.
```
```
Caso queira somente desenvolver o algoritmo em python basta excluir todas as partes do webservice.
```

### Instalando

Basta clonar o diretório, ou baixar manualmente e executar o arquivo .py desejado.
Para ser possível a execução será necessário a modificação de alguns arquivos para abstrair a parte de webservice utilizada pelo aplicativo.


## Testando

Há 2 arquivos que podem ser testados:
### Parser.py
Para testar basta implementar um hardcoded da sua gramática dentro do algoritmo e a frase que será reconhecida pelo parser. Ele retornará se foi, ou não reconhecida.
### Generator.py
Este necessita apenas da gramática hardcoded e a partir disso toda vez que for executado


## Arquivos Explicados
```
generator.py = Arquivo gerador de frases a partir de uma gramática previamente dada (Utiliza Early)

formais.py = Arquivo gerador de frases a partir de uma gramática previamente dada no texto "sample.txt" (Não utiliza Early)

input.py = Arquivo leitor do sample.txt

parser.py = Arquivo reconhecedor de uma frase a partir de uma gramática previamente dada no texto "sample.txt"

*Class.py = Classes que são importadas nos outros arquivos

*.apk = Aplicativo pronto

sample.txt = Arquivo input com o formato correto para testes é necessário ser desse formato.
```

## Lançamento

Dia XX/07/2017 durante a aula de Linguagens Formais e Autômatos

## Autores

* **Leonardo Vianna** - *Python Developer* - (https://github.com/vianna274)

* **Andy Ruiz Garramones** - *Python Developer* - (https://github.com/Andy9822)

* **João Vitor de Camargo** - *Android Developer* - (https://github.com/jvdecamargo)

* **Marlize Ramos** - *Grammar Creator* - (https://github.com/lizerb)

* **Matheus Rhoden** - *Support* - (https://github.com/matheusrhoden)