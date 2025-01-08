import pygame
from Config import screen_width, screen_height

from Sprites import all_sprites , bullets,  aliens, alien_bullets

class Ship(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.sprites = []
        spriteShip_files = [
            'StarShipStandard.png', 'StarShipShooting1.png', 'StarShipShooting2.png', 'StarShipShooting3.png',
            'StarShipShooting4.png', 'StarShipShooting5.png', 'StarShipShooting6.png', 'StarShipShooting7.png'
        ]
        for sprite_file in spriteShip_files:
            sprite = pygame.image.load(sprite_file)
            sprite = pygame.transform.scale(sprite, (75, 55))  # Redimensiona para 75x55 pixels
            self.sprites.append(sprite)
        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [350, 500]

        self.shooting = False
        self.shooting_counter = 0
        self.shooting_speed = 5 # Velocidade da animação de tiro
        self.cooldown = 0
        

    def update(self, elapsed_time, dead_aliens):
        keys = pygame.key.get_pressed()
        
        if elapsed_time <= 1:
            self.cooldown = 0
        self.handle_movement(keys)
        self.handle_shooting(keys, elapsed_time)
        if elapsed_time == 0:
            self.rect.topleft = [350, 500]
            self.cooldown = 0
    def handle_movement(self, keys):
        if keys[pygame.K_a]:
            self.rect.x -= 4
        if keys[pygame.K_d]:
            self.rect.x += 4

        # Mantém o sprite dentro da tela
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width

    
    def handle_shooting(self, keys, elapsed_time):


        # Animação de tiro
        if keys[pygame.K_SPACE] and (self.cooldown) < elapsed_time:
            self.shooting = True
            self.cooldown = (elapsed_time + 0.5)
            if self.shooting_counter == 0:  # Dispara um projétil
                bullet = Bullet(self.rect.centerx, self.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)

        if self.shooting:
            self.shooting_counter += 1
            if self.shooting_counter >= self.shooting_speed:
                self.shooting_counter = 0
                self.current_sprite += 1

                if self.current_sprite >= len(self.sprites):
                    self.current_sprite = 0
                    self.shooting = False  # Para a animação de tiro

                self.image = self.sprites[self.current_sprite]
        else:
            self.image = self.sprites[0]  # Sprite padrão quando não está atirando

            
class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill((255, 0, 0))  # Cor vermelha para o projétil
        self.rect = self.image.get_rect()
        self.rect.centerx = pos_x
        self.rect.top = pos_y
        self.speed_y = -7 # Velocidade de movimento vertical

    def update(self, elapsed_time, dead_aliens):
        self.rect.y += self.speed_y

        # Remove o sprite quando sair da tela
        if self.rect.bottom < 0:
            self.kill()

class Ship2(Ship):
    def __init__(self):
        super().__init__()
        self.rect.topleft = [350, 500]

    def handle_movement(self, keys):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 4
        if keys[pygame.K_RIGHT]:
            self.rect.x += 4

        # Mantém o sprite dentro da tela
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
    def handle_shooting(self, keys, elapsed_time):
        
        
        # Animação de tiro
        if keys[pygame.K_RCTRL] and (self.cooldown) < elapsed_time:
            self.shooting = True
            self.cooldown = (elapsed_time + 0.5)
            if self.shooting_counter == 0:  # Dispara um projétil
                bullet = Bullet(self.rect.centerx, self.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)

        if self.shooting:
            self.shooting_counter += 1
            if self.shooting_counter >= self.shooting_speed:
                self.shooting_counter = 0
                self.current_sprite += 1

                if self.current_sprite >= len(self.sprites):
                    self.current_sprite = 0
                    self.shooting = False  # Para a animação de tiro

                self.image = self.sprites[self.current_sprite]
        else:
            self.image = self.sprites[0]  # Sprite padrão quando não está atirando
