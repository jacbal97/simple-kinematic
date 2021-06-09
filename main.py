import pygame
from pygame.locals import *
from figure import figure

pygame.init()

size = width, height = 600, 480
screen = pygame.display.set_mode(size)

screen.fill('black')
pygame.display.flip()
