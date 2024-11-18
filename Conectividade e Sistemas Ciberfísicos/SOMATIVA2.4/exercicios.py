#!/usr/bin/env python3
from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
from datetime import datetime


def fazLog(msg: str):
    '''
    Registra em um log a mensagem recebida
    - Não altere essa função
    - O arquivo log.txt deve sem entregue como resultado da tarefa
    - O log é único para cada equipe pois inclui portas aleatórias e horário de cada evento     
    '''
    print(msg, end='')
    f = open('log.txt', 'a')
    f.write(f'{datetime.now()} : {msg}')
    f.close()

def exercicio1(porta: int):
    '''
    Crie o socket do servidor UDP que irá se comunicar com os dispositivos de IoT

    Parametros:
    porta: porta do servidor UDP
    '''
    s_udp = None   
    s_udp = socket(AF_INET, SOCK_DGRAM)  # SOCK_DGRAM é o tipo de socket UDP

    try:
        s_udp.bind(('localhost', porta))  # Associa o socket ao endereço e porta
    except:
        return None

    # -- Retorna o socket UDP criado
    return s_udp


def exercicio2(porta: int):
    '''
    Cria o socket do servidor TCP que irá funcionar como console para o usuário

    Parametros:
    porta: porta do servidor TCP
    '''
    s_tcp = None

    try:
        s_tcp = socket(AF_INET, SOCK_STREAM)  # Cria o socket TCP
        s_tcp.bind(('localhost', porta))  # Associa o socket ao endereço e porta
        s_tcp.listen(1)  # Coloca o socket em modo de escuta (backlog = 1)
    except:
        return None

    # -- Retorna o socket TCP criado
    return s_tcp



def exercicio3(s: socket, SENSORES: dict, comando: str):
    '''
    Envia o mesmo comando para todos os sensores
    
    Parametros:
    s: socket udp que se comunica com os sensores
    SENSORES: dicionario que associa o id do sensor e seu endereço
    commando: string com o comando para o usuário - precisa ser convertida para bytes
    '''

    # DICA: os endereços dos sensores registrados estão em SENSORES.values()
    # Faça um for para enviar o mesmo comando com sendto(bytes, endereço)
    
    #fazLog('esqueci de fazer o exercicio 3\n') # comente quando fizer o exercicio

    for sensor in SENSORES.values():
        s.sendto(comando.encode(), sensor)



def exercicio4(s: socket, sensor: str, estado: str, monitor: tuple):
    '''
    Envia o estado de um sensor para o monitor 
    - formato da mensagem: ESTADO sensor=estado\n
    
    Parametros:
    s: socket udp usado para se comunicar com o monitor
    sensor: id do dispositivo de IoT
    estado: string com o estado do sensor
    monitor: endereço do monitor (ip, porta)
    '''
    
    # DICA: monte a string a ser enviada f'ESTADO {sensor}={estado}\n'
    # converta para bytes
    # envie com s.sendto(bytes, addr)

    #fazLog('esqueci de fazer o exercicio 4\n') # comente quando fizer o exercicio

    estado_sensor = f'ESTADO {sensor}={estado}\n'
    s.sendto(estado_sensor.encode(), monitor)
    


def exercicio5(s: socket) -> tuple:
    '''
    Aguarda no máximo 60 segundos até receber uma mensagem.
     - Caso a mensagem seja recebida, retorna uma tupla (dados, endereco do transmissor)
     - Caso não seja recebida, retorna a tupla (None, None)
    
    Parametros:
    s: socket do tipo cliente usado pelo dispositivo de IoT
    '''
    
    try:
        s.settimeout(60)  # Seta o timeout para 60 segundos
        dados, endereco = s.recvfrom(1024)
        s.settimeout(None)  # Coloca o timeout no default após receber a mensagem
        return dados, endereco
    except:
        # fazLog('O monitor não responde')
        return None, None


if __name__ == "__main__":  
    print('ATENÇÃO: Você não deve executar exercicios.py, pois é uma biblioteca!')
    print('EXECUTE: monitor.py, sensores.py e usuario.py, nessa ordem')

    #---------------------------------------------------------------------
    # A ENTREGA DA SOMATIVA É ESTE ARQUIVO
    # COPIE O RESULTADO DO ARQUIVO log.txt E COLE ABAIXO PARA ENTREGAR A TAREFA

# 2024-10-09 21:14:27.898892 : MONITOR: aguardando dispositivos de IOT em 9999
# 2024-10-09 21:14:27.900942 : CONSOLE: aguardando conex�o do usu�rio em 8888
# 2024-10-09 21:14:34.552534 : MONITOR: o sensor sala registrou: ('127.0.0.1', 60319)
# 2024-10-09 21:14:34.552534 : SENSOR sala: registrou no Monitor ('127.0.0.1', 9999)
# 2024-10-09 21:14:34.583948 : SENSOR quarto: registrou no Monitor ('127.0.0.1', 9999)

# 2024-10-09 21:14:34.616695 : SENSOR cozinha: registrou no Monitor ('127.0.0.1', 9999)
# 2024-10-09 21:14:34.616695 : MONITOR: o sensor cozinha registrou: ('127.0.0.1', 60321)
# 2024-10-09 21:15:34.555790 : MONITOR: o sensor sala registrou: ('127.0.0.1', 60319)
# 2024-10-09 21:15:34.555790 : SENSOR sala: registrou no Monitor ('127.0.0.1', 9999)
# 2024-10-09 21:15:34.589239 : MONITOR: o sensor quarto registrou: ('127.0.0.1', 60320)
# 2024-10-09 21:15:34.618065 : SENSOR cozinha: registrou no Monitor ('127.0.0.1', 9999)
# 2024-10-09 21:15:34.618565 : MONITOR: o sensor cozinha registrou: ('127.0.0.1', 60321)
# 2024-10-09 21:15:41.569403 : CONSOLE: O usu�rio conectou
# 2024-10-09 21:15:41.672444 : CONSOLE RECEBEU: sala ligar
# 2024-10-09 21:15:41.672944 : IOT sala: recebeu o comando=ligar
# 2024-10-09 21:15:41.727848 : USUARIO RECEBEU: CONSOLE: digite SENSOR_ID COMANDO

# 2024-10-09 21:15:42.672712 : CONSOLE RECEBEU: sala consulta
# 2024-10-09 21:15:42.673213 : IOT sala: recebeu o comando=consulta
# 2024-10-09 21:15:42.674212 : MONITOR: sensor sala enviou sala=ON

# 2024-10-09 21:15:42.675213 : USUARIO RECEBEU: sensor sala enviou sala=ON

# 2024-10-09 21:16:34.605998 : SENSOR quarto: registrou no Monitor ('127.0.0.1', 9999)
# 2024-10-09 21:16:34.605998 : MONITOR: o sensor quarto registrou: ('127.0.0.1', 60320)
# 2024-10-09 21:16:34.620666 : SENSOR cozinha: registrou no Monitor ('127.0.0.1', 9999)
# 2024-10-09 21:16:34.620666 : MONITOR: o sensor cozinha registrou: ('127.0.0.1', 60321)
# 2024-10-09 21:16:42.673053 : CONSOLE RECEBEU: todos ligar
# 2024-10-09 21:16:42.673553 : IOT sala: recebeu o comando=ligar
# 2024-10-09 21:16:42.674051 : IOT cozinha: recebeu o comando=ligar
# 2024-10-09 21:16:42.674051 : IOT quarto: recebeu o comando=ligar
# 2024-10-09 21:16:43.673449 : CONSOLE RECEBEU: todos consulta
# 2024-10-09 21:16:43.674449 : IOT cozinha: recebeu o comando=consulta
# 2024-10-09 21:16:43.674449 : IOT sala: recebeu o comando=consulta
# 2024-10-09 21:16:43.674949 : MONITOR: sensor cozinha enviou cozinha=ON

# 2024-10-09 21:16:43.675449 : MONITOR: sensor sala enviou sala=ON

# 2024-10-09 21:16:43.676600 : IOT quarto: recebeu o comando=consulta
# 2024-10-09 21:16:43.676600 : MONITOR: sensor quarto enviou quarto=ON

# 2024-10-09 21:16:43.677106 : USUARIO RECEBEU: sensor cozinha enviou cozinha=ON

# 2024-10-09 21:16:43.677606 : USUARIO RECEBEU: sensor sala enviou sala=ON
# sensor quarto enviou quarto=ON

# 2024-10-09 21:17:43.686742 : MONITOR: o sensor cozinha registrou: ('127.0.0.1', 60321)
# 2024-10-09 21:17:43.686742 : SENSOR cozinha: registrou no Monitor ('127.0.0.1', 9999)
# 2024-10-09 21:17:43.687247 : SENSOR sala: registrou no Monitor ('127.0.0.1', 9999)
# 2024-10-09 21:17:43.687247 : MONITOR: o sensor sala registrou: ('127.0.0.1', 60319)
# 2024-10-09 21:17:43.687746 : SENSOR quarto: registrou no Monitor ('127.0.0.1', 9999)
# 2024-10-09 21:17:43.688247 : MONITOR: o sensor quarto registrou: ('127.0.0.1', 60320)
# 2024-10-09 21:18:43.690420 : MONITOR: o sensor cozinha registrou: ('127.0.0.1', 60321)
# 2024-10-09 21:18:43.690919 : SENSOR cozinha: registrou no Monitor ('127.0.0.1', 9999)
# 2024-10-09 21:18:43.690919 : MONITOR: o sensor sala registrou: ('127.0.0.1', 60319)
# 2024-10-09 21:18:43.690919 : SENSOR sala: registrou no Monitor ('127.0.0.1', 9999)
# 2024-10-09 21:18:43.691953 : MONITOR: o sensor quarto registrou: ('127.0.0.1', 60320)
# 2024-10-09 21:18:43.692428 : SENSOR quarto: registrou no Monitor ('127.0.0.1', 9999)


