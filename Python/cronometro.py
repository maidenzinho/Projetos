import time
import os

crono = int(input("Digite o tempo(Em segundos): "))

while crono > 0:
    crono -= 1
    print(crono)
    time.sleep(1)
    os.system('clear') # se estiver utilizando linux
    os.system('cls') # se estiver utilizando o windows

print("Tempo esgotado!")