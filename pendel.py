import pygame
import numpy as np
import time
import os

class Pendel:
    def __init__(self, length, start_position, start_angle, mass, luft_motstand):
        self.length = length
        self.start_position = start_position
        self.start_angle = np.radians(start_angle)
        self.position = self.start_pos() 
        
        self.mass = mass
        self.velocity = 0
        self.acceleration = pygame.Vector2(0, 0)
        self.gravitation = 9.81

        self.luftmotstand = luft_motstand
        self.angle = self.start_angle


    def start_pos(self):
        end_pos_vec = pygame.math.Vector2(-np.cos(self.start_angle) * self.length, np.sin(self.start_angle) * self.length) + self.start_position  
        return pygame.Vector2(round(end_pos_vec.x), round(end_pos_vec.y))

    def calc_acceleration(self):
        print(-self.luftmotstand * self.velocity**2)
        luftmotstandskraft = -self.luftmotstand * self.velocity * abs(self.velocity)
        self.acceleration = -(self.gravitation * np.sin(self.angle) -luftmotstandskraft)/self.length
        return self.acceleration
    
    def update_position(self):
        position_x = self.length * np.sin(self.angle) +self.start_position.x 
        position_y = self.length * np.cos(self.angle) +self.start_position.y

        self.position = pygame.Vector2(position_x, position_y)

    def update(self, dt):
        a = self.calc_acceleration() * dt

        self.velocity += a
        self.angle += self.velocity
        self.update_position()

if __name__ == "__main__": 
    os.system("python main.py")