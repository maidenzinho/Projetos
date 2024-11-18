#!/usr/bin/env python3
from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
from threading import Thread
import exercicios as EX  
import os
from console import Console

# ---------------------------------------------------------------------------------------------
# UMA UNICA THREAD PARA TODOS OS SENSORES
def TrataSensor(s: socket, SENSORES: dict, CONSOLE: list): 
   
    '''
    Recebe mensagens vindas dos dispositivos de IoT
    - atualiza o dicionario SENSORES
    - repassa as mensagens recebidas para a Thread Console

    Parametros:
    s: socket UDP que se comunica com os dispositivos de IoT
    SENSORES: dicionario com os sensores registrados
    CONSOLE: lista que contém a conexão de console com o usuário
    '''

    while True:
        data, addr = s.recvfrom(1024)
        strdata =  data.decode()
        try:
            comando, dado = strdata.split(' ',1)
        except:
            EX.fazLog(f'MONITOR: recebi mensagem invalida {strdata} de {addr}\n')
            continue
        if comando == 'REGISTRO':
            SENSORES[dado] = addr
            s.sendto('ACKregistro'.encode(), addr )
            EX.fazLog(f'MONITOR: o sensor {dado} registrou: {addr}\n')
        elif comando == 'ESTADO':
            if addr not in SENSORES.values():
                id = 'DESCONHECIDO'
            else:
                for id,a in SENSORES.items():
                    if a == addr:
                        break
            EX.fazLog(f'MONITOR: sensor {id} enviou {dado}\n')
            CONSOLE[0].send(f'sensor {id} enviou {dado}'.encode())
            
#--------------------------------------------------------------------------------
# MAIN THREAD


if __name__ == "__main__":    

    if os.path.exists("log.txt"): os.remove("log.txt")

    PORTA_IOT = 9999
    SENSORES = {} # dicionário é mutável
    CONSOLE =[None] # lista é mutável

    # Lança o servidor TCP que funciona como console
    s = EX.exercicio1(PORTA_IOT)
    if s is None:
        EX.fazLog(f'MONITOR: erro no exercício 1\n')        
    else:    
        EX.fazLog(f'MONITOR: aguardando dispositivos de IOT em {PORTA_IOT}\n')
        Thread(target=Console, args=(CONSOLE, SENSORES, s)).start()     
        TrataSensor(s, SENSORES, CONSOLE)




