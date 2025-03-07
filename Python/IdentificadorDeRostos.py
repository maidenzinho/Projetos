import cv2
import numpy as np
from pyfirmata2 import Arduino

# Configuração do Arduino
port = "COM3"  # porta que utilizei na IDE arduino
board = Arduino(port)
servoX = board.get_pin('d:7:s')  # Servo conectado no pino 7
servoY = board.get_pin('d:10:s')  # Servo conectado no pino 10

# Posições iniciais dos servos
current_servoX = 90  # Centralizado
current_servoY = 90
servoX.write(current_servoX)
servoY.write(current_servoY)

# Configuração do OpenCV
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not cap.isOpened():
    print("Câmera não pode ser acessada.")
    exit()

frame_width = 1024
frame_height = 1024
cap.set(3, frame_width)
cap.set(4, frame_height)

# Função para mapear valores (similar ao map() do Arduino)
def map_value(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# Zona morta para movimentos pequenos
dead_zone = 10  # Pixels

# Variáveis para média móvel
history_size = 5  # Número de leituras para calcular a média
x_history = []
y_history = []

# Loop principal
while True:
    ret, frame = cap.read()
    if not ret:
        print("Erro ao capturar a imagem.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) > 0:
        # Detecta o rosto principal (primeiro da lista)
        x, y, w, h = faces[0]
        face_center_x = x + w // 2
        face_center_y = y + h // 2

        # Adiciona a posição atual ao histórico
        x_history.append(face_center_x)
        y_history.append(face_center_y)

        # Mantém o histórico limitado
        if len(x_history) > history_size:
            x_history.pop(0)
        if len(y_history) > history_size:
            y_history.pop(0)

        # Calcula a média das posições para suavizar
        avg_x = sum(x_history) / len(x_history)
        avg_y = sum(y_history) / len(y_history)

        # Verifica se o movimento é maior que a zona morta
        delta_x = abs(avg_x - (frame_width / 2))
        delta_y = abs(avg_y - (frame_height / 2))

        if delta_x > dead_zone:
            target_servoX = map_value(avg_x, 0, frame_width, 180, 40)
            current_servoX = max(40, min(180, target_servoX))
            servoX.write(current_servoX)

        if delta_y > dead_zone:
            target_servoY = map_value(avg_y, 0, frame_height, 20, 180)
            current_servoY = max(20, min(180, target_servoY))
            servoY.write(current_servoY)

        # Desenha o círculo no rosto detectado
        radius = max(w, h) // 3  # Define o raio do círculo com base no tamanho do rosto
        cv2.circle(frame, (face_center_x, face_center_y), radius, (0, 255, 0), 2)  # Círculo

        # Desenha as linhas da mira
        cv2.line(frame, (face_center_x, 0), (face_center_x, frame_height), (0, 255, 0), 2)  # Linha vertical
        cv2.line(frame, (0, face_center_y), (frame_width, face_center_y), (0, 255, 0), 2)  # Linha horizontal

        # Desenha a bolinha vermelha no centro
        cv2.circle(frame, (face_center_x, face_center_y), 5, (0, 0, 255), -1)  # Bolinha vermelha no centro

        # Mostra as coordenadas na tela
        cv2.putText(frame, f"Servo X: {int(current_servoX)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
        cv2.putText(frame, f"Servo Y: {int(current_servoY)}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    # Exibe o vídeo com a detecção de rosto
    cv2.imshow("Face Tracking", frame)

   