import pygame
import pygame as pg
import random

# pg.init()

# largura_tela = 400
# altura_tela = 600
# tela = pg.display.set_mode((largura_tela, altura_tela))
# # start_ticks = pg.time.get_ticks()  # starter tick

# valor_inicial = 1
# meta = random.randint(0,100)
# branco = (255, 255, 255)
# vermelho = (255, 45, 45)
# fonte = pg.font.Font('assets/fonts/pixel-art.ttf', 20)  # Fonte para exibir o contador

# # Lista de operações matemáticas
# operacoes = ["+", "-", "x", "/"]  # Use "x" para representar multiplicação


# class ScoreBoard:
#     #iniciando os valorem em 0
#     def __init__(self):
#         self.scores = {
#             "+": 0,
#             "-": 0,
#             "x": 0,
#             "/": 0
#         }

#     def increment (self, operation, value):
#         if operation in self.scores:
#             self.scores[operation] += 1
#     def display(self, surface, font, x_offset, y_offset):
#             for operacao, score in self.scores.items():
#                 score_surface = font.render(f"{operacao}: {score}", True, vermelho)
#                 surface.blit(score_surface, (x_offset, y_offset))
#                 y_offset += 30

# class Coletavel:
#     def __init__(self):
#         self.x = random.randint(0, largura_tela)
#         self.y = 0
#         self.velocidade = 0.1  # Defina uma velocidade constante
#         self.operacao = random.choice(operacoes)  # Escolha aleatória de operação
#         self.operando = random.randint(1, 10)  # Número aleatório pro operando
#         self.resposta = self.calcular_resposta()

#     # def calcular_opercao(self):
#     #     operacao = random.choice(operacoes)  # Escolha aleatória de operação
#     #     operando = random.randint(1, 10)  # Número aleatório pro operando
#     #     resultado = valor_inicial
#     #     while True:
            
#     #         if operacao == "+":
#     #             resultado += operando
#     #         elif operacao == "-":
#     #             resultado -= operando
#     #         elif operacao == "x":
#     #             resultado *= operando
#     #         elif operacao == "/":
#     #             resultado /= operando

#     #         if resultado == meta:
#     #             break
#     #         else:
#     #             # Se o resultado não atingir a meta, escolha outra operação aleatória
#     #             operacao = random.choice(operacoes)
#     #             operando = random.randint(1, 10)

#     #     return operacao, operando
    
#     def calcular_resposta(self):
#         resposta = valor_inicial  # Inicialize com o valor_inicial
#         if self.operacao == "+":
#             resposta += self.operando
#         elif self.operacao == "-":
#             resposta -= self.operando
#         elif self.operacao == "x":
#             resposta *= self.operando
#         elif self.operacao == "/":
#             resposta /= self.operando
            
#         return resposta

#     def mover(self):
#         self.y += self.velocidade

#     def desenhar_objeto(self):
#         objeto_surface = fonte.render(f"{self.operacao} {self.operando}", True, branco)
#         objeto_rect = objeto_surface.get_rect(center=(self.x + 10, self.y + 10))
#         tela.blit(objeto_surface, objeto_rect)

# objetos_caindo = []
# contador = 0
# intervalo_geracao = 2000
# limite_geracao = intervalo_geracao

# # # Posição inicial do jogador
# # jogador_x = largura_tela // 2 - 20
# # jogador_y = altura_tela - 40
# # jogador_velocidade = 5  # Velocidade de movimento do jogador

# # Jogador
# jogador_largura = 50
# jogador_altura = 20
# jogador_x = (largura_tela - jogador_largura) // 2
# jogador_y = altura_tela - jogador_altura
# velocidade_jogador = 1

# scoreboard = ScoreBoard()

# executando = True
# while executando:
#     for evento in pygame.event.get():
#         if (evento.type == pygame.QUIT) or (evento.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_ESCAPE]):
#             executando = False
#             break

#     if contador < limite_geracao:
#         contador += 1
#     else:
#         novo_objeto = Coletavel()
#         objetos_caindo.append(novo_objeto)
#         contador = 0
#         limite_geracao = random.randint(1, intervalo_geracao)

#     for objeto in objetos_caindo:
#         objeto.mover()

#     tela.fill((0, 0, 0))

#     for objeto in objetos_caindo:
#         objeto.desenhar_objeto()

#     jogador_rect = pygame.Rect(jogador_x, jogador_y, jogador_largura, jogador_altura)
#     pygame.draw.rect(tela, branco, jogador_rect)

#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT] and jogador_x > 0:
#         jogador_x -= velocidade_jogador
#     if keys[pygame.K_RIGHT] and jogador_x < largura_tela - jogador_largura:
#         jogador_x += velocidade_jogador

#     for objeto in objetos_caindo:
#         objeto_rect = pygame.Rect(objeto.x, objeto.y, 20, 20)
#         if jogador_rect.colliderect(objeto_rect):
#             if objeto.operacao == "+":
#                 valor_inicial += objeto.operando
#             elif objeto.operacao == "-":
#                 valor_inicial -= objeto.operando
#             elif objeto.operacao == "x":
#                 valor_inicial *= objeto.operando
#             elif objeto.operacao == "/":
#                 valor_inicial /= objeto.operando
#             scoreboard.increment(objeto.operacao)
#             objetos_caindo.remove(objeto)

#     texto_meta = fonte.render(f"Meta: {meta}", True, branco)
#     tela.blit(texto_meta, (250, 10))
#     valor_surface = fonte.render(f"Valor: {valor_inicial}", True, branco)
#     tela.blit(valor_surface, (10, 10))

#     x_offset = 10
#     y_offset = 40
#     scoreboard.display(tela, fonte, x_offset, y_offset)

#     if valor_inicial >= meta:
#         executando = False

#     pygame.display.flip()

# pygame.quit()
import pygame
import random

pygame.init()

largura_tela = 400
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))

valor_inicial = 1
meta = random.randint(0,100)
branco = (255, 255, 255)
fonte = pygame.font.Font('assets/fonts/pixel-art.ttf', 20)

operacoes = ["+", "-", "x", "/"]

class ScoreBoard:
    def __init__(self):
        self.scores = {
            "+": 0,
            "-": 0,
            "x": 0,
            "/": 0
        }

    def increment(self, operation):
        if operation in self.scores:
            self.scores[operation] += 1

    def display(self, surface, font, x_offset, y_offset):
        for operacao, score in self.scores.items():
            score_surface = font.render(f"{operacao}: {score}", True, branco)
            surface.blit(score_surface, (x_offset, y_offset))
            y_offset += 30

class Coletavel:
    def __init__(self):
        self.x = random.randint(0, largura_tela)
        self.y = 0
        self.velocidade = 0.1
        self.operacao = random.choice(operacoes)
        self.operando = random.randint(1, 10)
        self.resposta = self.calcular_resposta()

    def calcular_resposta(self):
        resposta = valor_inicial
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
intervalo_geracao = 2000
limite_geracao = intervalo_geracao

jogador_largura = 50
jogador_altura = 20
jogador_x = (largura_tela - jogador_largura) // 2
jogador_y = altura_tela - jogador_altura
velocidade_jogador = 1

scoreboard = ScoreBoard()

executando = True
while executando:
    for evento in pygame.event.get():
        if (evento.type == pygame.QUIT) or (evento.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_ESCAPE]):
            executando = False
            break

    if contador < limite_geracao:
        contador += 1
    else:
        novo_objeto = Coletavel()
        objetos_caindo.append(novo_objeto)
        contador = 0
        limite_geracao = random.randint(1, intervalo_geracao)

    for objeto in objetos_caindo:
        objeto.mover()

    tela.fill((0, 0, 0))

    for objeto in objetos_caindo:
        objeto.desenhar_objeto()

    jogador_rect = pygame.Rect(jogador_x, jogador_y, jogador_largura, jogador_altura)
    pygame.draw.rect(tela, branco, jogador_rect)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and jogador_x > 0:
        jogador_x -= velocidade_jogador
    if keys[pygame.K_RIGHT] and jogador_x < largura_tela - jogador_largura:
        jogador_x += velocidade_jogador

    for objeto in objetos_caindo:
        objeto_rect = pygame.Rect(objeto.x, objeto.y, 20, 20)
        if jogador_rect.colliderect(objeto_rect):
            valor_inicial = objeto.resposta
            scoreboard.increment(objeto.operacao)
            objetos_caindo.remove(objeto)

    texto_meta = fonte.render(f"Meta: {meta}", True, branco)
    tela.blit(texto_meta, (250, 10))
    valor_surface = fonte.render(f"Valor: {valor_inicial}", True, branco)
    tela.blit(valor_surface, (10, 10))

    x_offset = 10
    y_offset = 40
    scoreboard.display(tela, fonte, x_offset, y_offset)

    if valor_inicial >= meta:
        executando = False

    pygame.display.flip()

pygame.quit()
