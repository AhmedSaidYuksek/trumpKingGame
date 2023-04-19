import pygame

class Card:
  suit = None
  value = None
  image = None

  def __init__(self, suit, value):
    self.suit = suit
    self.value = value
    self.image = pygame.image.load('images/' + self.suit.name + '-' + str(self.value) + '.svg')