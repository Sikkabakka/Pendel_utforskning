import pygame
import numpy as np
import time
import os

class Pendel:
    def __init__(self, length, start_position, start_angle, mass, luft_motstand = 0):
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
        end_pos_vec = pygame.Vector2(-np.cos(self.start_angle) * self.length, np.sin(self.start_angle) * self.length) + self.start_position  
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

class Doublependel():


    def __init__(self, length, start_position, start_angle, mass):
        self.p1 = Pendel(length, start_position, start_angle, mass)
        self.p2 = Pendel(length, self.p1.position, start_angle, mass)
    def update(self, dt):
        g = 9.81
        num1 = -g * (2 * self.p1.mass + self.p2.mass) * np.sin(self.p1.angle)
        num2 = -self.p1.mass * g * np.sin(self.p1.angle - 2 * self.p2.angle)
        num3 = -2 * np.sin(self.p1.angle - self.p2.angle) * self.p2.mass
        num4 = np.square(self.p2.velocity) * self.p2.length + np.square(self.p1.velocity) * self.p1.length * np.cos(self.p1.angle - self.p2.angle)
        den = self.p1.length * (2 * self.p1.mass + self.p2.mass - self.p2.mass * np.cos(2 * self.p1.angle - 2 * self.p2.angle))
        
        self.p1.acceleration = (num1 + num2 + num3 * num4) / den * dt
        print(self.p1.acceleration)
        #p1.aAcc må du sjekke ut
        num1 = 2 * np.sin(self.p1.angle - self.p2.angle)
        num2 = np.square(self.p1.velocity) * self.p1.length * (self.p1.mass + self.p2.mass)
        num3 = g * (self.p1.mass + self.p2.mass) * np.cos(self.p1.angle)
        num4 = np.square(self.p2.velocity) * self.p2.length * self.p2.mass * np.cos(self.p1.angle - self.p2.angle)
        den = self.p2.length * (2 * self.p1.mass + self.p2.mass - self.p2.mass * np.cos(2 * self.p1.angle - 2 * self.p2.angle))

        self.p2.acceleration = (num1 * (num2 + num3 + num4)) / den *dt


       
        self.p1.velocity += self.p1.acceleration
        self.p1.angle += self.p1.velocity
        self.p1.position.x = self.p1.length * np.sin(self.p1.angle) + self.p1.start_position.x
        self.p1.position.y = self.p1.length * np.cos(self.p1.angle) + self.p1.start_position.y

        self.p2.start_position = self.p1.position
        self.p2.velocity += self.p2.acceleration
        self.p2.angle += self.p2.velocity
        self.p2.position.x = self.p2.length * np.sin(self.p2.angle) + self.p2.start_position.x
        self.p2.position.y = self.p2.length * np.cos(self.p2.angle) + self.p2.start_position.y


if __name__ == "__main__": 
    os.system("python main.py")