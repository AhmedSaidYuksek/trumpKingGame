import pygame
from enum import Enum
import random

DEFAULT_IMAGE_SIZE = (58, 83)


class Suits(Enum):
  CLUB = 0
  SPADE = 1
  HEART = 2
  DIAMOND = 3

class Deck:
  cards = None
  
  def __init__(self):
    self.cards = []
    for suit in Suits:
      for value in range(1,14):
        if value==1:
          self.cards.append(Card(suit, (value+13)))
        else:  
          self.cards.append(Card(suit, value))
  def shuffle(self):
    random.shuffle(self.cards)
    
  def deal(self,number):
    return self.cards[number]

  def length(self):
    return len(self.cards)

class Card:
  suit = None
  value = None
  cost = None
  image = None

  def __init__(self, suit, value):
    self.suit = suit
    self.value = value    
    if self.suit.name=='CLUB':
        self.cost=value+60
    elif self.suit.name=='SPADE':
        self.cost=value+20
    elif self.suit.name=='HEART':
        self.cost=value+40 
    elif self.suit.name=='DIAMOND':
        self.cost=value 
    self.image = pygame.image.load('./images/' + self.suit.name + '-' + str(self.value) + '.svg')
    self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)