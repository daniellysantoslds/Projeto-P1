import pygame as pg
import random

# class Timer():
    #  def __init__(self):
        #  self.tempo_inicial = pg.time.get_ticks()
        #  self.tempo_limite_segundos = 90 
        #  self.tempo_atual = pg.time.get_ticks()  # Tempo atual em milissegundos
        #  self.tempo_decorrido_segundos = (self.tempo_atual - self.tempo_inicial) // 1000  # Tempo decorrido em segundos
        #  self.tempo_restante = max(self.tempo_limite_segundos - self.tempo_decorrido_segundos, 0)  # Tempo restante em segundos
        

class TimerGame:
    def __init__(self):
        self.tempo_inicial = pg.time.get_ticks()
        self.tempo_limite_segundos = 90
        self.meta = random.randint(0, 100)
        self.valor_inicial = 1

    def atualizar(self):
        tempo_atual = pg.time.get_ticks()
        tempo_decorrido_segundos = (tempo_atual - self.tempo_inicial) // 1000
        tempo_restante = max(self.tempo_limite_segundos - tempo_decorrido_segundos, 0)
        return tempo_restante