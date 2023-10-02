import pygame as pg
import random
from timer import TimerGame
from pplayer import Player
from coletavel import Coletavel, ScoreBoard

# Inicialização do pygame
pg.init()

# Configurações da tela
largura_tela = 400
altura_tela = 600
tela = pg.display.set_mode((largura_tela, altura_tela))
pg.display.set_caption("NumFall")

tempo_inicial = pg.time.get_ticks()
tempo_limite_segundos = 90
meta = random.randint(1, 100)
valor_inicial = 1
branco = (255, 255, 255)

fonte = pg.font.Font('assets/fonts/pixel-art.ttf', 20)
fonte_títulos = pg.font.Font('assets/fonts/FiraCode.ttf', 32)
fonte_restart = pg.font.Font('assets/fonts/FiraCode.ttf', 15)
fonte_objetos = pg.font.Font('assets/fonts/pixel-art.ttf', 15)

objetos_caindo = []

contador = 0
pontuacao = 0
intervalo_geracao = 5000
limite_geracao = intervalo_geracao

scoreboard = ScoreBoard()
jogo = TimerGame()
player = Player(largura_tela, altura_tela)


def reiniciar_jogo():
    global objetos_caindo, pontuacao, valor_inicial, contador, limite_geracao, meta
    objetos_caindo = []
    pontuacao = 0
    valor_inicial = 1
    contador = 0
    limite_geracao = intervalo_geracao
    meta = random.randint(0, 100)

# Função para exibir a tela de início de jogo
def tela_inicio_jogo():
    executando = True
    while executando:
        for evento in pg.event.get():
            if (evento.type == pg.QUIT) or (evento.type == pg.KEYDOWN and pg.key.get_pressed()[pg.K_ESCAPE]):
                pg.quit()
                exit()
            if evento.type == pg.MOUSEBUTTONDOWN:
                if botao_jogar.collidepoint(evento.pos):
                    return

        tela.fill((0, 0, 0))
        texto_inicio = fonte_títulos.render("NumFall", True, (43, 255, 0))
        tela.blit(texto_inicio, (135, 75))
        botao_jogar = pg.Rect(120, 300, 150, 50)
        pg.draw.rect(tela, (43, 255, 0), botao_jogar)
        texto_jogar = fonte_títulos.render("Play", True, (0, 0, 0))
        tela.blit(texto_jogar, (160, 305))
        pg.display.flip()


# Função para exibir a tela de fim de jogo
def tela_fim_de_jogo():
    executando = True
    while executando:
        for evento in pg.event.get():
            if (evento.type == pg.QUIT) or (evento.type == pg.KEYDOWN and pg.key.get_pressed()[pg.K_ESCAPE]):
                pg.quit()
                exit()
            if evento.type == pg.MOUSEBUTTONDOWN:
                if botao_reiniciar.collidepoint(evento.pos):
                    reiniciar_jogo()
                    return
                
        tela.fill((0, 0, 0))
        
        
        texto_fim = fonte_títulos.render(f"Game Over", True, (43, 255, 0))
        texto_pts = fonte_títulos.render(f'Score:{pontuacao}', True, (43, 255, 0))
        tela.blit(texto_fim, (100, 50))
        tela.blit(texto_pts, (100, 120))
        
        botao_reiniciar = pg.Rect(120, 300, 150, 50)
        pg.draw.rect(tela, (43, 255, 0), botao_reiniciar)
        texto_reiniciar = fonte_títulos.render("Restart", True, (0, 0, 0))
        tela.blit(texto_reiniciar, (125, 305))
        pg.display.flip()

# Exibe a tela de início de jogo
tela_inicio_jogo()

executando = True
while executando:
    for evento in pg.event.get():
        if (evento.type == pg.QUIT) or (evento.type == pg.KEYDOWN and pg.key.get_pressed()[pg.K_ESCAPE]):
            executando = False
            #pg.quit()
            #exit()

    tela.fill((0, 0, 0))

    # Funções do timer:
    tempo_restante = jogo.atualizar()
    player.desenhar(tela)

    if contador < limite_geracao:
        contador += 1

    else:
        novo_objeto = Coletavel()
        objetos_caindo.append(novo_objeto)
        contador = 0

        limite_geracao = random.randint(1, intervalo_geracao)

    for objeto in objetos_caindo:
        objeto.mover()
        objeto.desenhar_objeto()

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        player.mover_esquerda()
    if keys[pg.K_RIGHT]:
        player.mover_direita()

    for objeto in objetos_caindo:
        objeto_rect = pg.Rect(objeto.x, objeto.y, 20, 20)
        if player.colliderect(objeto_rect):
            pontuacao += 1
            valor_inicial = objeto.calcular_resposta()
            scoreboard.increment(objeto.operacao)
            objetos_caindo.remove(objeto)

    texto_meta = fonte.render(f"Meta: {meta}", True, branco)
    tela.blit(texto_meta, (largura_tela - 110, 10))

    valor_surface = fonte.render(f"Valor: {valor_inicial:.2f}", True, branco)
    tela.blit(valor_surface, (10, 10))

    texto_tempo = fonte.render(f"{tempo_restante}s", True, branco)
    tela.blit(texto_tempo, ((largura_tela/2), 10))

    x_offset = 10
    y_offset = 40
    scoreboard.display(tela, fonte, x_offset, y_offset)

    if valor_inicial == meta or tempo_restante == 0:
        executando = False
        tela_fim_de_jogo()

    pg.display.flip()

pg.quit()
