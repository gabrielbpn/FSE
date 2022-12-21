# FSE - TRABALHO 1

- Este trabalho tem por objetivo a criação de um sistema distribuído de automação predial para monitoramento e acionamento de sensores e dispositivos de um prédio com múltiplas salas.

- Essa solução contém:

- Conexão com o servidor distribuído (TCP/IP);
- Uma interface que mantenham atualizadas as seguintes informações:
a. Estado das entradas (Sensores);
b. Estado das Saídas (lâmpadas, aparelhos de ar, etc.);
c. Valor da temperatura e umidade de cada sala a cada 2 segundos;
d. Contador de Ocupação (Número de Pessoas) presentes no prédio como um todo e a ocupação individual de cada sala;
Prover mecanismo na interface para:
a. Acionar manualmente lâmpadas, aparelhos de ar-condicionado e projetores das salas;
b. Acionamento do sistema de alarme que, quando estiver ligado, deve tocar um som de alerta (acionar a sirene/buzzer) ao detectar presenças ou abertura de portas/janelas;
c. Acionamento de alarme de incêncio que, ao detectar presença de fumaça a qualquer momento deve soar o alarme;

- Manter os valores de temperatura e umidade atualizados a cada 2 segundos (Sendo requisitado pelo servidor central periodicamente ou enviado via mensagem push);
- Aciona Lâmpadas, aparelhos de Ar-Condicionado e projetores (mantendo informação sobre seu estado) conforme comandos do Servidor Central e retornando uma mensagem de confirmação para o mesmo sobre o sucesso ou não do acionamento;
- Mantém o estado dos sensores de presença e abertura de portas/janelas informando ao servidor central imediatamente (mensagem push) quando detectar o acionamento de qualquer um deles;
- Mantém o estado dos sensores de fumaça informando ao servidor central imediatamente (mensagem push) quando detectar o acionamento de qualquer um deles;
- Efetua a contagem de pessoas entrando e saindo da sala para controle de ocupação;

## Arquivos

Servidor Central: central.py
Servidor distribuido: distribuido.py
new.py: arquivo principal que trata as funções do GPIO nas placas 2 e 4
new2.py: arquivo principal que trata as funções do GPIO nas placas 1 e 3

## Como rodar

1) Clone o repositório.
- git clone https://github.com/gabrielbpn/FSE.git

2) Vá para a pasta onde você clonou - não entre na pasta do git.

3) Envie para a rasp

- scp -r -P 13508 -r FSE <user_>@<000.00.00.00>:~

4) Entre na rasp e vá para a pasta FSE

5) Abra dois terminais e rode:
- ssh python3 central.py <ip_da_placa>
- ssh python3 distribuido.py <ip_da_placa>

## Apresentação

- Link: https://youtu.be/hFdFdso3yYk
