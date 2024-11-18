
#!/usr/bin/env python3
from socket import socket, AF_INET, SOCK_DGRAM
import time
from multiprocessing import Process
from threading import Thread
import exercicios as EX

IP_MONITOR = '127.0.0.1'
PORTA_IOT = 9999
ESTADO = 'OFF'

def interpretaComando(id: str, comando: str, s : socket):
    global ESTADO
    EX.fazLog(f'IOT {id}: recebeu o comando={comando}\n')
    if comando.lower() == 'ligar':
        ESTADO = 'ON'
    elif comando.lower() == 'desligar':
        ESTADO = 'OFF'
    elif comando.lower() == 'consulta':
        EX.exercicio4(s, id, ESTADO, (IP_MONITOR, PORTA_IOT) )
    elif comando.lower() == 'shutdown':
        s.close()  
        EX.fazLog(f'IoT {id}: recebi um shutdow. Bye!!!\n')
        exit()  
    else:
        EX.fazLog(f'IoT {id}: comando desconhecido = {comando}\n')
        time.sleep(10)

def registraIoT(s: socket, id, addr):
    s.sendto( f'REGISTRO {id}'.encode(), addr)

    resultado = False

    try:
        s.settimeout(5)
        data, addr = s.recvfrom(1024)
        if data.decode() == 'ACKregistro':
            EX.fazLog(f'SENSOR {id}: registrou no Monitor {addr}\n')
            resultado = True
        else:
            EX.fazLog(f'SENSOR {id}: recebi uma mensagem invalida de {addr}\n')
    except:
        EX.fazLog(f'SENSOR {id}: o monitor esta desligado')
    
    s.settimeout(None)
    return resultado

def main_sensor(ip: str, porta: int, id: str):

    '''
    Programa principal executado pelo dispositivo de IoT

    Parametros:
    ip: endereço do monitor
    porta: porta do monitor
    id: identificado do dispositivo de IoT
    '''

    s = socket(AF_INET, SOCK_DGRAM)
    monitor = (IP_MONITOR, PORTA_IOT)

    while True:
        if registraIoT(s, id, monitor ):
            break
        else:
            time.sleep(10)

    while True:

        dados, addr = EX.exercicio5(s)

        if dados == None:
            registraIoT(s, id, monitor)
        
        elif addr != (IP_MONITOR, PORTA_IOT):
            EX.fazLog(f'SENSOR: recebi uma mensagem de origem desconhecida: {addr}\n')

        else:
            interpretaComando(id, dados.decode(), s)  

#--------------------------------------------------------------
if __name__ == '__main__':
    Process(target=main_sensor, args=(IP_MONITOR, PORTA_IOT,'sala')).start()
    Process(target=main_sensor, args=(IP_MONITOR, PORTA_IOT,'quarto')).start()
    Process(target=main_sensor, args=(IP_MONITOR, PORTA_IOT,'cozinha')).start()
    print('Os dispositivos de IoT foram lançados')
