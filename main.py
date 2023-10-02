# Inicializando os pacotes necessários
import random
import pygame as pg
from sys import exit
# Importando as clases
from pplayer import Player
from coletavel import Coletavel, ScoreBoard
from timer import TimerGame


def main():
    # Iniciando o pygame
    pg.init()
    
    # Iniciando as constantes de tela
    Largura_tela = 400
    Altura_tela = 600
    tela = pg.display.set_mode((Largura_tela, Altura_tela))
    
    # Constantes do jogo e contadores
    meta = random.randint(1, 100)
    valor_inicial = 1
    branco = (255, 255, 255)
    verde = (43, 255, 0)
    
    contador = 0
    pontuacao = 0
    intervalo_geracao = 3000
    limite_geracao = intervalo_geracao
    objetos_caindo = []
    
    # Título da janela
    pg.display.set_caption('NumFall')
    
    # Acessando as fontes da interface de jogo
    fonte_interface_jogo = pg.font.Font('assets/fonts/pixel-art.ttf', 20)
    fonte_objetos = pg.font.Font('assets/fonts/pixel-art.ttf', 15)
    
    # Acessando as fontes das telas de começo e fim de jogo
    fonte_títulos = pg.font.Font('assets/fonts/FiraCode.ttf', 32)
    fonte_restart = pg.font.Font('assets/fonts/FiraCode.ttf', 15)
    
    # Chamando as clases do Timer, do scoreboard e o player
    timer = TimerGame()
    scoreboard = ScoreBoard()
    player = Player(Largura_tela, Altura_tela)
    coletavel = Coletavel()
    
    executando= True
    while executando:
        # Métodos de saída do laço do jogo
        for evento in pg.event.get():
            if (evento.type == pg.QUIT) or (evento.type == pg.KEYDOWN and pg.key.get_pressed()[pg.K_ESCAPE]):
                executando = False
                pg.quit()
                exit()

        tela.fill((0, 0, 0))
        # Funções do timer
        tempo_restante = timer.atualizar()
        
        # Desenhando o jogador na tela
        player.desenhar(tela)
        
        # Gerando os novos objetos na tela
        if contador < limite_geracao:
            contador += 1
        else:
            novo_objeto = coletavel
            objetos_caindo.append(novo_objeto)
            contador = 0
            
            limite_geracao = random.randint(1, intervalo_geracao)
        # Desenhando os objetos na tela
        for objeto in objetos_caindo:
            objeto.mover()
            objeto.desenhar_objeto()
        
        key = pg.key.get_pressed()
        
        # Movimentação do jogador
        if key[pg.K_LEFT]:
            player.mover_esquerda()
        if key[pg.K_RIGHT]:
            player.mover_direita()
        
        # Colisão do jogador com os objetos
        for objeto in objetos_caindo:
            objeto_rect = pg.Rect(objeto.x, objeto.y, 20, 20)
            if player.colliderect(objeto_rect):
                pontuacao += 1
                valor_inicial = objeto.calcular_resposta()
                scoreboard.increment(objeto.operacao)
                objetos_caindo.remove(objeto)
        
        # Interface
        ## Meta
        texto_meta = fonte_interface_jogo.render(f'Target: {meta}', True, branco)
        tela.blit(texto_meta, ((Largura_tela - 110), 10))
        
        ## Valor inicial
        texto_val_inicial = fonte_interface_jogo.render(f'Value: {valor_inicial:.2f}', True, branco)
        tela.blit(texto_val_inicial, (10, 10))
        
        ## Timer
        texto_timer = fonte_interface_jogo.render(f'{tempo_restante}s', True, branco)
        tela.blit(texto_timer, ((Largura_tela/2), 10))
        
        ## Scoreboard
        scoreboard.display(tela, fonte_interface_jogo, 10, 40)
        
        if valor_inicial == meta or tempo_restante == 0:
            print("Game Over")
            executando = False
            # chamar a tela de fim de jogo
            
        pg.display.flip()
        
        pg.quit()

main()