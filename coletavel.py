import pygame as pg
import random

pg.init()
largura_tela = 400
altura_tela = 600
tela = pg.display.set_mode((largura_tela, altura_tela))
start_ticks = pg.time.get_ticks()  # starter tick

valor_inicial = 1
meta = random.randint(0,100)
branco = (255, 255, 255)
fonte = pg.font.Font('assets/fonts/pixel-art.ttf', 20)  # Fonte para exibir o contador]

# Lista de operações matemáticas
operacoes = ["+", "-", "x", "/"]  # Use "x" para representar multiplicação

class Coletavel:
    def __init__(self):
        self.x = random.randint(0, largura_tela)
        self.y = 0
        self.velocidade = 0.1  # Defina uma velocidade constante
        self.operacao = random.choice(operacoes)  # Escolha aleatória de operação
        self.operando = random.randint(1, 10)  # Número aleatório pro operando
        
        self.resposta = self.calcular_resposta()

    def calcular_opercao(self):
        operacao = random.choice(operacoes)  # Escolha aleatória de operação
        operando = random.randint(1, 10)  # Número aleatório pro operando
        resultado = valor_inicial
        while True:
            
            if operacao == "+":
                resultado += operando
            elif operacao == "-":
                resultado -= operando
            elif operacao == "x":
                resultado *= operando
            elif operacao == "/":
                resultado /= operando

            if resultado == meta:
                break
            else:
                # Se o resultado não atingir a meta, escolha outra operação aleatória
                operacao = random.choice(operacoes)
                operando = random.randint(1, 10)

        return operacao, operando
    
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

# Posição inicial do jogador
jogador_x = largura_tela // 2 - 20
jogador_y = altura_tela - 40
jogador_velocidade = 5  # Velocidade de movimento do jogador

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

    for objeto in objetos_caindo:
        objeto.mover()

    tela.fill((0, 0, 0))

    for objeto in objetos_caindo:
        objeto.desenhar_objeto()

    jogador_rect = pg.Rect(largura_tela // 2 - 20, altura_tela - 40, 40, 40)  # Posição e tamanho do jogador
    pg.draw.rect(tela, branco, jogador_rect)

    # Lógica de movimento do jogador
    teclas = pg.key.get_pressed()
    if teclas[pg.K_LEFT]:
        jogador_x -= jogador_velocidade
    if teclas[pg.K_RIGHT]:
        jogador_x += jogador_velocidade
        
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
    valor_surface = fonte.render(f"Valor: {valor_inicial}", True, branco)
    tela.blit(valor_surface, (10, 10))

    # Verifique se o jogador atingiu a meta
    if valor_inicial >= meta:
        executando = False

    pg.display.flip()

pg.quit()