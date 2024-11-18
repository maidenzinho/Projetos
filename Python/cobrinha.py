import pygame
import time
import random

# Inicialize o Pygame
pygame.init()

# Configurações da tela cheia
LARGURA, ALTURA = pygame.display.Info().current_w, pygame.display.Info().current_h
TELA = pygame.display.set_mode((LARGURA, ALTURA), pygame.FULLSCREEN)
pygame.display.set_caption('Jogo da Cobrinha')

# Cores
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
BRANCO = (255, 255, 255)

# Configurações da cobrinha
TAMANHO_COBRA = 20
VELOCIDADE_COBRA = 15

# Fonte
FONTE = pygame.font.SysFont(None, 35)

def mostrar_mensagem(msg, cor, posicao):
    texto = FONTE.render(msg, True, cor)
    TELA.blit(texto, posicao)

def menu():
    menu_ativo = True
    while menu_ativo:
        TELA.fill(PRETO)
        mostrar_mensagem("Bem-vindo ao Jogo da Cobrinha", BRANCO, [LARGURA / 4, ALTURA / 3 - 50])
        mostrar_mensagem("Pressione ENTER para começar", BRANCO, [LARGURA / 4, ALTURA / 3])
        mostrar_mensagem("Pressione Q para sair", BRANCO, [LARGURA / 4, ALTURA / 3 + 50])
        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    menu_ativo = False
                if evento.key == pygame.K_q:
                    pygame.quit()
                    quit()

def gameLoop():
    fim_jogo = False
    acabou = False

    x_cobra = LARGURA / 2
    y_cobra = ALTURA / 2

    x_cobra_mudanca = 0
    y_cobra_mudanca = 0

    comida_x = round(random.randrange(0, LARGURA - TAMANHO_COBRA) / TAMANHO_COBRA) * TAMANHO_COBRA
    comida_y = round(random.randrange(0, ALTURA - TAMANHO_COBRA) / TAMANHO_COBRA) * TAMANHO_COBRA

    relogio = pygame.time.Clock()
    
    cobra = []
    comprimento_cobra = 1

    pontos = 0

    while not fim_jogo:

        while acabou:
            TELA.fill(PRETO)
            mostrar_mensagem("Você perdeu! Pressione Q para sair ou C para jogar novamente", VERMELHO, [LARGURA / 6, ALTURA / 3])
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        fim_jogo = True
                        acabou = False
                    if evento.key == pygame.K_c:
                        gameLoop()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x_cobra_mudanca = -TAMANHO_COBRA
                    y_cobra_mudanca = 0
                elif evento.key == pygame.K_RIGHT:
                    x_cobra_mudanca = TAMANHO_COBRA
                    y_cobra_mudanca = 0
                elif evento.key == pygame.K_UP:
                    y_cobra_mudanca = -TAMANHO_COBRA
                    x_cobra_mudanca = 0
                elif evento.key == pygame.K_DOWN:
                    y_cobra_mudanca = TAMANHO_COBRA
                    x_cobra_mudanca = 0

        if x_cobra >= LARGURA or x_cobra < 0 or y_cobra >= ALTURA or y_cobra < 0:
            acabou = True
        x_cobra += x_cobra_mudanca
        y_cobra += y_cobra_mudanca
        TELA.fill(PRETO)
        pygame.draw.rect(TELA, VERDE, [comida_x, comida_y, TAMANHO_COBRA, TAMANHO_COBRA])
        cobra_cabeca = []
        cobra_cabeca.append(x_cobra)
        cobra_cabeca.append(y_cobra)
        cobra.append(cobra_cabeca)
        if len(cobra) > comprimento_cobra:
            del cobra[0]

        for segmento in cobra[:-1]:
            if segmento == cobra_cabeca:
                acabou = True

        for segmento in cobra:
            pygame.draw.rect(TELA, VERDE, [segmento[0], segmento[1], TAMANHO_COBRA, TAMANHO_COBRA])

        mostrar_mensagem(f"Pontos: {pontos}", BRANCO, [10, 10])

        pygame.display.update()

        if x_cobra == comida_x and y_cobra == comida_y:
            comida_x = round(random.randrange(0, LARGURA - TAMANHO_COBRA) / TAMANHO_COBRA) * TAMANHO_COBRA
            comida_y = round(random.randrange(0, ALTURA - TAMANHO_COBRA) / TAMANHO_COBRA) * TAMANHO_COBRA
            comprimento_cobra += 1
            pontos += 1

        relogio.tick(VELOCIDADE_COBRA)

    pygame.quit()
    quit()

if __name__ == "__main__":
    menu()
    gameLoop()
