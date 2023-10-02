import pygame as pg

class Player:
    def __init__(self, largura_tela, altura_tela):
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela
        self.largura = 50
        self.altura = 20
        self.x = (self.largura_tela - self.largura) // 2
        self.y = self.altura_tela - self.altura
        self.velocidade = 0.2
    
    def colliderect(self, rect):
        # Verifique a colisão entre o jogador e um retângulo
        jogador_rect = pg.Rect(self.x, self.y, self.largura, self.altura)
        return jogador_rect.colliderect(rect)
    
    def mover_esquerda(self):
        if self.x > 0:
            self.x -= self.velocidade

    def mover_direita(self):
        if self.x < self.largura_tela - self.largura:
            self.x += self.velocidade

    def desenhar(self, tela):
        jogador_rect = pg.Rect(self.x, self.y, 40, 40)  # Posição e tamanho do jogador
        pg.draw.rect(tela, (255,255,255), jogador_rect)