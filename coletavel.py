import pygame as pg
import random

pg.init()
largura_tela = 400
altura_tela = 600
tela = pg.display.set_mode((largura_tela, altura_tela))
# start_ticks = pg.time.get_ticks()  # starter tick

tempo_inicial = pg.time.get_ticks()  # Tempo inicial em milissegundos
tempo_limite_segundos = 90  # Tempo limite em segundos
meta = random.randint(0,100)
valor_inicial = 1
branco = (255, 255, 255)
fonte = pg.font.Font('assets/fonts/pixel-art.ttf', 20)  # Fonte para exibir o contador
fonte_objetos = pg.font.Font('assets/fonts/pixel-art.ttf', 15)
# Lista de operações matemáticas
operacoes = ["+", "-", "x", "/"]  #"x" para representar multiplicação

class Coletavel:
    def __init__(self):
        self.x = random.randint(0, largura_tela - 20)
        self.y = 0
        self.velocidade = 0.07  # Defina uma velocidade constante
        self.operacao = random.choice(operacoes)  # Escolha aleatória de operação
        self.operando = random.randint(1, 10)  # Número aleatório pro operando
        self.resposta = self.calcular_resposta()

    def calcular_resposta(self):
        resposta = valor_inicial
        # Determinando a operação
        if self.operacao == "+":
            resposta += self.operando
            
        elif self.operacao == "-":
            resposta -= self.operando
            
        elif self.operacao == "x":
            resposta *= self.operando
            
        elif self.operacao == "/":
            resposta /= self.operando
            
        return resposta

    def mover(self):
        self.y += self.velocidade

    def desenhar_objeto(self):
        objeto_surface = fonte_objetos.render(f"{self.operacao} {self.operando}", True, branco)
        objeto_rect = objeto_surface.get_rect(center=(self.x + 10, self.y + 10))
        tela.blit(objeto_surface, objeto_rect)

objetos_caindo = []


contador = 0
pontuacao = 0
intervalo_geracao = 2200  # Defina o intervalo de geração (menos objetos ao mesmo tempo)
limite_geracao = intervalo_geracao 

# Jogador
jogador_largura = 50
jogador_altura = 20
jogador_x = (largura_tela - jogador_largura) // 2
jogador_y = altura_tela - jogador_altura
velocidade_jogador = 0.3

executando = True
while executando:
    for evento in pg.event.get():
        if (evento.type == pg.QUIT) or (evento.type == pg.KEYDOWN and pg.key.get_pressed()[pg.K_ESCAPE]):
            executando = False
            break
    
    # Funções do timer:
    tempo_atual = pg.time.get_ticks()  # Tempo atual em milissegundos
    tempo_decorrido_segundos = (tempo_atual - tempo_inicial) // 1000  # Tempo decorrido em segundos
    tempo_restante = max(tempo_limite_segundos - tempo_decorrido_segundos, 0)  # Tempo restante em segundos

    if contador < limite_geracao:
        contador += 1

    else:
        novo_objeto = Coletavel()
        objetos_caindo.append(novo_objeto)
        contador = 0

        limite_geracao = random.randint(1, intervalo_geracao)
        
    tela.fill((0, 0, 0))

    for objeto in objetos_caindo:
        objeto.mover()
        objeto.desenhar_objeto()

    jogador_rect = pg.Rect(jogador_x, jogador_y, 40, 40)  # Posição e tamanho do jogador
    jogador = pg.draw.rect(tela, branco, jogador_rect)

    # Capturar entrada do teclado
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and jogador_x > 0:
        jogador_x -= velocidade_jogador
    if keys[pg.K_RIGHT] and jogador_x < largura_tela - jogador_largura:
        jogador_x += velocidade_jogador
        
    # Verifique colisões
    for objeto in objetos_caindo:
        objeto_rect = pg.Rect(objeto.x, objeto.y, 20, 20)
        if jogador_rect.colliderect(objeto_rect):
            pontuacao += 1
            valor_inicial = objeto.calcular_resposta()  # Sem argumentos
            objetos_caindo.remove(objeto)

    # Exiba o valor inicial e a meta na tela
    texto_meta = fonte.render(f"Meta: {meta}", True, branco)
    tela.blit(texto_meta, (largura_tela - 110, 10))
    
    # Exiba o valor inicial na tela
    valor_surface = fonte.render(f"Valor: {valor_inicial:.2f}", True, branco)
    tela.blit(valor_surface, (10, 10))

    # Exiba o tempo restante na tela
    texto_tempo = fonte.render(f"{tempo_restante}s", True, branco)
    tela.blit(texto_tempo, ((largura_tela/2), 10))  # Posicione o texto onde você deseja na tela

    # Verifique se o jogador atingiu a meta
    if valor_inicial == meta or tempo_restante == 0:
        executando = False

    pg.display.flip()

pg.quit()