import pygame
from Config import screen_width, screen_height
import Player 
from Sprites import all_sprites , bullets,  aliens, alien_bullets

class Alien(pygame.sprite.Sprite):
    alienCount = 1
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        sprite_files = [ 
            [
            'Sprite-0002.png', 'Sprite-0003.png', 'Sprite-0004.png', 
            'Sprite-0005.png', 'Sprite-0006.png', 'Sprite-0007.png', 
            'Sprite-0008.png', 'Sprite-0009.png', 'Sprite-0010.png', 
            'Sprite-0011.png'
            ],

            [
                'Sprite-Jellyfish-0001.png', 'Sprite-Jellyfish-0002.png', 'Sprite-Jellyfish-0003.png', 
                'Sprite-Jellyfish-0004.png', 'Sprite-Jellyfish-0005.png', 'Sprite-Jellyfish-0006.png', 
                'Sprite-Jellyfish-0007.png', 'Sprite-Jellyfish-0008.png', 'Sprite-Jellyfish-0009.png' 
            ],
            [
                'Sprite-Breadhead-0001.png', 'Sprite-Breadhead-0002.png', 'Sprite-Breadhead-0003.png',
            ]

        ]

        if pos_y == 0:
            selected_sprite = sprite_files[0]
        elif pos_y >= 80 and pos_y <= 160:
            selected_sprite = sprite_files[1]
        else:
            selected_sprite = sprite_files[2]

        for sprite_file in selected_sprite:
            sprite = pygame.image.load(sprite_file)
            sprite = pygame.transform.scale(sprite, (75, 55))  # Redimensiona para 75x55 pixels
            self.sprites.append(sprite)
        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

        self.animation_speed = 5  # Velocidade da animação (quanto maior, mais lenta)
        self.frame_counter = 0
        self.speed_x = 1  # Velocidade de movimento horizontal

        self.count = 1 # Contador para movimento vertical

        self.rect = pygame.Rect(pos_x, pos_y, 75, 55)  # Exemplo de retângulo para o alien
        Alien.alienCount = 1
              

    def update(self, elapsed_time, dead_aliens):
        self.frame_counter += 1
       
        # print(dead_aliens)
        # print(f"Velocidade: {self.speed_x} rigth {self.rect.right} width {screen_width} left {self.rect.left}") 
        self.time = int(elapsed_time)

        if self.frame_counter >= self.animation_speed:
            self.frame_counter = 0
            self.current_sprite += 1

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0

            self.image = self.sprites[self.current_sprite]

        # Movimento horizontal
        self.rect.x += self.speed_x

        # Mantém o sprite dentro da tela
        if self.rect.right > screen_width or self.rect.left < 0:
            self.speed_x = -self.speed_x
            
        if self.time == 0:
            self.speed_x = 1
            self.count = 1

        # Movimento vertical
        if (self.time/3) == (3*self.count): #9 18 27 36 45  
            self.rect.y += 0.5
            
        
        if dead_aliens == Alien.alienCount*8:
            for alien in aliens:
                if alien.speed_x > 0:
                    alien.speed_x += 3
                else:
                    alien.speed_x -= 3
        
        if dead_aliens >= Alien.alienCount*8:    
            Alien.alienCount += 1
           
         
        
        if (self.time/3) > (3*self.count): 
            self.count += 1

        if self.rect.y >= 500:
            self.rect.x = Player.rect.x
        ##Debugg movimento vertical
        # tempo = (self.time/4)
        # contador = (self.count*4)
        # print(f"Tempo:{tempo} Contador:{contador} velocidade{self.speed_x}")    

    def on_collision(self):
        # Lógica para lidar com a colisão
        # print(f"Colisão detectada no sprite em posição {self.rect.topleft}")
        
        self.speed_x = -self.speed_x  # Inverte a direção do movimento

   
    def shoot(self):
        bullet = AlienBullet(self.rect.centerx, self.rect.bottom)
        all_sprites.add(bullet)
        alien_bullets.add(bullet)

class AlienBullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill((0, 0, 255))  # Cor verde para o projétil do alien
        self.rect = self.image.get_rect()
        self.rect.centerx = pos_x
        self.rect.top = pos_y

    def update(self, elapsed_time, dead_aliens):
        self.rect.y += 5  # Velocidade da bala
        if self.rect.top > screen_height or elapsed_time < 1:
            self.kill()  # Remove a bala se sair da tela
