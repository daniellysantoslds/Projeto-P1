import pygame as pg
import random

pg.init()
largura_tela = 400
altura_tela = 600
tela = pg.display.set_mode((largura_tela, altura_tela))
# start_ticks = pg.time.get_ticks()  # starter tick

meta = random.randint(0,100)
valor_inicial = 1
branco = (255, 255, 255)
fonte = pg.font.Font('assets/fonts/pixel-art.ttf', 20)  # Fonte para exibir o contador
# Lista de operações matemáticas
operacoes = ["+", "-", "x", "/"]  #"x" para representar multiplicação

class Coletavel:
    def __init__(self):
        self.x = random.randint(0, largura_tela)
        self.y = 0
        self.velocidade = 0.1  # Defina uma velocidade constante
        self.operacao = random.choice(operacoes)  # Escolha aleatória de operação
        self.operando = random.randint(1, 10)  # Número aleatório pro operando
        self.resposta = self.calcular_resposta()

    def calcular_resposta(self):
        resposta = valor_inicial  # Inicialize com o valor_inicial
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
        objeto_surface = fonte.render(f"{self.operacao} {self.operando}", True, branco)
        objeto_rect = objeto_surface.get_rect(center=(self.x + 10, self.y + 10))
        tela.blit(objeto_surface, objeto_rect)

objetos_caindo = []

contador = 0
pontuacao = 0
intervalo_geracao = 2000  # Defina o intervalo de geração (menos objetos ao mesmo tempo)
limite_geracao = intervalo_geracao 

# Jogador
jogador_largura = 50
jogador_altura = 20
jogador_x = (largura_tela - jogador_largura) // 2
jogador_y = altura_tela - jogador_altura
velocidade_jogador = 1

executando = True
while executando:
    for evento in pg.event.get():
        if (evento.type == pg.QUIT) or (evento.type == pg.KEYDOWN and pg.key.get_pressed()[pg.K_ESCAPE]):
            executando = False
            break

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
            valor_inicial = objeto.resposta  # Atualize o valor inicial com a resposta do objeto
            objetos_caindo.remove(objeto)

    # Exiba o valor inicial e a meta na tela
    texto_meta = fonte.render(f"Meta: {meta}", True, branco)
    tela.blit(texto_meta, (250, 10))
    
    # Exiba o valor inicial na tela
    valor_surface = fonte.render(f"Valor: {valor_inicial:.2f}", True, branco)
    tela.blit(valor_surface, (10, 10))

    # Verifique se o jogador atingiu a meta
    if valor_inicial == meta:
        executando = False

    pg.display.flip()

pg.quit()