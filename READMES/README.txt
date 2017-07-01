Com toda a lógica de geração e interpretação de gramáticas realizadas no Python 2.7, 
utilizamos a biblioteca web.py para fazer com o nosso gerador pudesse atuar como um serviço web.
Dessa forma, disponibilizamos um serviço que, ao receber uma requisição, retorna uma frase montada
pelo gerador. Esse serviço está hospedado em: http://jvdecamargo.pythonanywhere.com/. 
A plataforma Python Anywhere permite com que aplicações pequenas em Python sejam hospedadas
temporariamente de forma gratuita (nosso serviço ficará por mais 3 meses disponível). 
O arquivo generator.py é o "principal". Seu método principal faz com que a web.py inicialize 
um serviço que espera requisições. A cada nova requisição, uma nova frase é gerada. 
Atualize a página e verá que a frase muda.

Dessa forma, nosso cliente Android faz uma 
requisição pro endereço acima e recebe como resposta uma frase, que é mostrada (e narrada) 
para o usuário. O mesmo usuário então pode pedir outra frase, compartilhar a frase atual 
no WhatsApp, etc. Para rodar a aplicação, é só instalar o .apk entregue em um celular Android. 
Nossa aplicação já está apontando para o serviço e deverá lhe pedir seu nome e então começar a 
mostrar frases.