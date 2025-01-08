import pygame
import json
from Sprites import all_sprites , bullets,  aliens, alien_bullets
from Aliens import Alien

class _Method:
    def __init__(self):
         pass
    
    def create_alien(self, restart):
        if restart:
            # Limpar os grupos de sprites
            for alien in aliens:
                alien.kill()
                
        # Cria os aliens
        alien_positions = [0, 80, 160, 240, 320, 400, 480, 560]
        for y in range(0, 400, 80):  # Loop para as linhas (0, 80, 160, 240, 320)
            for x in range(8):  # Loop para as colunas (0 a 7)
                alien = Alien(alien_positions[x], y)
                all_sprites.add(alien)
                aliens.add(alien)
        
        return pygame.time.get_ticks()
    
    
    
    def restart_phase(self, dead_aliens,running, reset, life):
        
        if dead_aliens == 40:
            return True
        
        elif life == 0:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    return False
 
    

    def load_points(self, filename='assets/points.json'):
        try:
            with open(filename, 'r') as file:
                points = json.load(file)
        except FileNotFoundError:
            points = 0  # Se o arquivo não existir, inicialize os pontos com 0
        return points

    def save_points(self, points, filename='assets/points.json'):
        with open(filename, 'w') as file:
            json.dump(points, file)


    def show_collision_animation(self, screen, screen_width, screen_height):

        animation_frames = [
            pygame.image.load('assets/Game_over1.png'),
            pygame.image.load('assets/Game_over2.png'),
            pygame.image.load('assets/Game_over3.png'),
            pygame.image.load('assets/Game_over4.png'),
            pygame.image.load('assets/Game_over5.png'),
        ]

        # Redimensionar cada frame da animação para preencher toda a tela
        scaled_frames = [pygame.transform.scale(frame, (800, 600)) for frame in animation_frames]

        # Exibir cada frame da animação
        for frame in scaled_frames:
            screen.blit(frame, (0, 0))  # Desenha a imagem redimensionada na posição (0, 0)
            pygame.display.flip()
            pygame.time.delay(100) 



    def restart_game(self, running, reset):

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                reset = False


            elif event.type == pygame.QUIT:
                running = False
                reset = False


        return running, reset




    @property
    def dead_aliens(self):

        return self._dead_aliens