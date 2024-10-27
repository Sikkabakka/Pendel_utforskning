import pygame
import numpy as np


pygame.init()

width = 800
height = 800
default_start = (width/2, 50)
background_color = "white"
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pendel GUD")

pygame.display.update()




running = True
class Pendel:
    def __init__(self, length, start_position, start_angle, mass):
        self.length = length
        self.start_position = start_position
        self.start_angle = np.radians(start_angle)
        self.position = self.start_pos(self.length, start_angle, self.start_position) 
        
        self.mass = mass
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0)
        self.gravitation = 9.81
        self.end_pos_vector = self.position - self.start_position
        
    def start_pos(self, length, start_angle, start_position):
        end_pos_vec = pygame.math.Vector2(-np.cos(self.start_angle) * length, np.sin(self.start_angle) * length) + start_position  
        return pygame.Vector2(round(end_pos_vec.x), round(end_pos_vec.y))
    
    def test_move(self):
        self.position = (self.position[0], self.position[1])
    
    def get_angle_to_top(self):
        downwards_vector = pygame.Vector2(0, self.length)
        
        
        dot_product = self.end_pos_vector.dot(downwards_vector)
        
        lengde_product = self.end_pos_vector.length() * downwards_vector.length()
       
        angle = np.arccos(dot_product/lengde_product)

        return angle

    def calc_acceleration(self):
        self.acceleration = self.gravitation * np.sin(self.get_angle_to_top())


        normal_vector = pygame.Vector2(-self.end_pos_vector.y , self.end_pos_vector.x).normalize()
        return normal_vector * self.acceleration/100
    
        
    def update(self):
        self.velocity += self.calc_acceleration()
        self.position += self.velocity + self.start_position
        self.position = self.position.normalize() *self.length
        self.end_pos_vector = self.position - self.start_position
        
        
        
def draw_pendel(start_position, end_position, radius = 5):
    pygame.draw.line(screen, "grey", start_position, end_position, 2)
    pygame.draw.circle(screen, "black", end_position, radius)

pendel = Pendel(100, pygame.Vector2(width/2, 50), 60, 1)
while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False
    screen.fill(background_color) 
    draw_pendel(default_start, (pendel.position.x, pendel.position.y))
 
    pendel.update()
    pygame.display.update()