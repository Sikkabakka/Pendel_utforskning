from pendel import *

import os
class Tester:

    def __init__(self,  window, pendel_top):
        self.window = window
        self.multiple_pendel = False
        self.double_pendel = False
        self.list_of_pendels = []
        self.pendel_top = pendel_top

    def draw_pendel(self, start_position, end_position, radius = 5):
        pygame.draw.line(self.window, "grey", start_position, end_position, 2)
        pygame.draw.circle(self.window, "black", end_position, radius)

    def multiple_pendels(self, amount, spacing, first_space, starting_angle = 45):
        self.list_of_pendels = []
        for i in range(amount):
            self.list_of_pendels.append(Pendel(spacing* (i)+first_space,self.pendel_top, starting_angle, 10, 0))
        self.multiple_pendel = True

    def make_double_pendel(self):
        first_pendel = Pendel(50, self.pendel_top, 45, 1, 1)
        second_pendel = Pendel(50, first_pendel.position , 45, 1, 1)

        pass

    def run(self):
        TARGET_FPS = 60
        clock = pygame.time.Clock()
        running = True
        while running:
            dt = clock.tick(TARGET_FPS) / 1000.0  
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
            self.window.fill("white") 

            if self.multiple_pendel:
                for pendel in self.list_of_pendels:
                    self.draw_pendel(self.pendel_top, (pendel.position.x, pendel.position.y))
                    pendel.update(dt)

            pygame.display.update()
        
if __name__ == "__main__": 
    os.system("python main.py")