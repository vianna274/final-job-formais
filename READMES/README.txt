Com toda a l�gica de gera��o e interpreta��o de gram�ticas realizadas no Python 2.7, 
utilizamos a biblioteca web.py para fazer com o nosso gerador pudesse atuar como um servi�o web.
Dessa forma, disponibilizamos um servi�o que, ao receber uma requisi��o, retorna uma frase montada
pelo gerador. Esse servi�o est� hospedado em: http://jvdecamargo.pythonanywhere.com/. 
A plataforma Python Anywhere permite com que aplica��es pequenas em Python sejam hospedadas
temporariamente de forma gratuita (nosso servi�o ficar� por mais 3 meses dispon�vel). 
O arquivo generator.py � o "principal". Seu m�todo principal faz com que a web.py inicialize 
um servi�o que espera requisi��es. A cada nova requisi��o, uma nova frase � gerada. 
Atualize a p�gina e ver� que a frase muda.

Dessa forma, nosso cliente Android faz uma 
requisi��o pro endere�o acima e recebe como resposta uma frase, que � mostrada (e narrada) 
para o usu�rio. O mesmo usu�rio ent�o pode pedir outra frase, compartilhar a frase atual 
no WhatsApp, etc. Para rodar a aplica��o, � s� instalar o .apk entregue em um celular Android. 
Nossa aplica��o j� est� apontando para o servi�o e dever� lhe pedir seu nome e ent�o come�ar a 
mostrar frases.