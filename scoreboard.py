import pygame as pg
import random

verde = (143, 81, 53)

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
            score_surface = font.render(f"{operacao}: {score}", True, verde)
            surface.blit(score_surface, (x_offset, y_offset))
            y_offset += 30