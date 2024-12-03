import pygame
import numpy as np
import time
from tester import Tester
pygame.init()

width = 700
height = 700
default_start = pygame.Vector2(width/2, 50)
background_color = "white"
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pendel GUD")

pygame.display.update()



tester = Tester(screen, pygame.Vector2(width/2, 50))
# tester.multiple_pendels( 10, 40, 40)


tester.make_double_pendel(-60, 90, 100, 100, 1, 10)
tester.run()

pygame.quit()

