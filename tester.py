from pendel import *

import os
class Tester:

    def __init__(self,  window, pendel_top):
        self.window = window

        self.list_of_pendels = 0
        self.pendel_top = pendel_top
        self.double_pendel = 0
    def draw_pendel(self, start_position, end_position, radius = 5):
        pygame.draw.line(self.window, "grey", start_position, end_position, 2)
        pygame.draw.circle(self.window, "black", end_position, radius)

    def multiple_pendels(self, amount, spacing, first_space, starting_angle = 45):
        self.list_of_pendels = []
        for i in range(amount):
            self.list_of_pendels.append(Pendel(spacing* (i)+first_space,self.pendel_top, starting_angle, 10, 0))

    def make_double_pendel(self, starting_angle, second_starting_angle, first_length, second_length, first_mass, second_mass):
        self.double_pendel = Doublependel(first_length, second_length,  self.pendel_top, starting_angle, second_starting_angle, first_mass, second_mass)

    def run(self):
        FPS = 60
        clock = pygame.time.Clock()
        running = True
        while running:
            dt = clock.tick(FPS) / 1000.0  
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
            self.window.fill("white") 

            if self.list_of_pendels:
                for pendel in self.list_of_pendels:
                    self.draw_pendel(self.pendel_top, (pendel.position.x, pendel.position.y))
                    pendel.update(dt)
            if self.double_pendel:
                self.draw_pendel(self.double_pendel.p1.start_position, (self.double_pendel.p1.position.x, self.double_pendel.p1.position.y ), 5)
                self.draw_pendel(self.double_pendel.p2.start_position, (self.double_pendel.p2.position.x, self.double_pendel.p2.position.y ), 5)
                self.double_pendel.update(dt)

            pygame.display.update()
        
if __name__ == "__main__": 
    os.system("python main.py")