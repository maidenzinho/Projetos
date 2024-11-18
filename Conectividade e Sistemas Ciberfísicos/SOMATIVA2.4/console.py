from socket import socket, AF_INET, SOCK_STREAM
import exercicios as EX 

PORTA_CONSOLE = 8888

def Console(CONSOLE: list, SENSORES: dict, s: socket):
  '''
  O console é uma thread que implementa as funções de comunicação com o usuário
  - Recebe comandos do usuário via Putty ou nc
  - Repassa as respostas dos sensores para o usuário
  - Atualiza a variável CONSOLE[0] com None quando o usuário não está conectado
  
  Parametros:
  CONSOLE: lista que irá conter a conexão TCP com o usuário na posição 0
  SENSORES: dicionario que associa o id do sensor e seu endereço (ip,porta)
  s: socket UDP usado para falar com os dispositivos de IoT
  '''
  
  s_tcp = EX.exercicio2(PORTA_CONSOLE)
  if s_tcp is None:
    EX.fazLog(f'CONSOLE: erro no exercício 2\n')
    return # encerra a Thread do console

  while True:
    EX.fazLog(f'CONSOLE: aguardando conexão do usuário em {PORTA_CONSOLE}\n')
    conn, _ = s_tcp.accept()
    EX.fazLog(f'CONSOLE: O usuário conectou\n')
    CONSOLE[0] = conn
   
    CONSOLE[0].send('CONSOLE: digite SENSOR_ID COMANDO\n'.encode()) 
    while True:
      data = CONSOLE[0].recv(200).decode()
      if not data:
        print('CONSOLE: O usuário desconectou')
        CONSOLE[0] = None
        break

      # Remove caracteres de quebra de linha
      for c in ['\r', '\n']: data = data.replace(c,'')
      if(len(data) == 0): continue #ignora quebras de linha
      
      data = data.split(' ', 1)
      if len(data) != 2:
        CONSOLE[0].send('COMANDO INCORRETO: Digite SENSOR_ID COMANDO\n'.encode()) 
      else:
        sensor, comando = data          

      try:
        EX.fazLog(f'CONSOLE RECEBEU: {sensor} {comando}\n')
        if sensor in SENSORES:
            s.sendto(comando.encode(), SENSORES[sensor])            
        elif sensor in ['todos','TODOS','broadcast','BROADCAST']:
            EX.exercicio3(s, SENSORES, comando)            
        else:
            CONSOLE[0].send(f'O sensor {sensor} nao existe\n'.encode())
            EX.fazLog(f'CONSOLE: O sensor {sensor} nao existe\n')
            msg = 'sensores conectados: ' + ', '.join(SENSORES.keys())
            CONSOLE[0].send(msg.encode())                          
      except Exception as e:
            print(e)

#---------------------------------------------------------------------------------------------
# MAIN THREAD

if __name__ == "__main__": 
  print('VOCE NÃO DEVE EXECUTAR O console.py! ISTO É UM MODULO.')