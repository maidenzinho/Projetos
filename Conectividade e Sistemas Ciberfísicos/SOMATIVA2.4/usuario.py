from socket import socket, AF_INET, SOCK_STREAM
from multiprocessing import Process
import time
import exercicios as EX

def recebeMensagem(s : socket):
    while True:
        try:
            data = s.recv(1024)
            if not data:
                EX.fazLog('USUARIO: O Monitor encerrou\n')
                break
            EX.fazLog(f'USUARIO RECEBEU: {data.decode()}\n')            
        except Exception as e:
            print('O Monitor encerrou')
            break

#-------------------------------------------------------
if __name__ == '__main__':

    PORTA_CONSOLE = 8888
    s = socket(AF_INET, SOCK_STREAM)

    try:
        s.connect(('127.0.0.1', PORTA_CONSOLE))
        t = Process(target=recebeMensagem, args=(s,))
        t.start()
        s.send('sala ligar\n'.encode())
        time.sleep(1)
        s.send('sala consulta\n'.encode())
        time.sleep(60)
        s.send('todos ligar\n'.encode())
        time.sleep(1)
        s.send('todos consulta\n'.encode())


        # Digite outros comandos de teste ou <ENTER> para terminar
        while True:
            msg = input()
            if not msg:
                break
            else:
                s.send( (msg+'\n').encode())
    except Exception as e:
        print(e)
        print('O Monitor está com problemas')
        