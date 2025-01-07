import pygame
import time
import random

class Alien(pygame.sprite.Sprite):
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
            
            
        if dead_aliens == 8:
            if self.speed_x > 0:
                self.speed_x += 3
            else:
                self.speed_x += -3
           
         
        
        if (self.time/3) > (3*self.count): 
            self.count += 1

        if self.rect.y >= 500:
            self.rect.x = player.rect.x
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
    

class Player(pygame.sprite.Sprite):
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

        if elapsed_time == 0:
            self.rect.topleft = [350, 500]
            self.cooldown = 0

        if keys[pygame.K_a]:
            self.rect.x -= 4
        if keys[pygame.K_d]:
            self.rect.x += 4

        # Mantém o sprite dentro da tela
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width

        

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

    def on_collision(self):
        # Lógica para lidar com a colisão

            print("Game Over")
            pygame.quit()

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
            
def show_collision_animation(screen, screen_width, screen_height):

    animation_frames = [
        pygame.image.load('Game_over1.png'),
        pygame.image.load('Game_over2.png'),
        pygame.image.load('Game_over3.png'),
        pygame.image.load('Game_over4.png'),
        pygame.image.load('Game_over5.png'),
    ]
    
    # Redimensionar cada frame da animação para preencher toda a tela
    scaled_frames = [pygame.transform.scale(frame, (800, 600)) for frame in animation_frames]
    
    # Exibir cada frame da animação
    for frame in scaled_frames:
        screen.blit(frame, (0, 0))  # Desenha a imagem redimensionada na posição (0, 0)
        pygame.display.flip()
        pygame.time.delay(100) 

def create_alien(restart):
    if restart:
        # Limpar os grupos de sprites
        for alien in aliens:
            alien.kill()
            print("Alien morto")
    
    # Cria os aliens
    alien_positions = [0, 80, 160, 240, 320, 400, 480, 560]
    for y in range(0, 400, 80):  # Loop para as linhas (0, 80, 160, 240, 320)
        for x in range(8):  # Loop para as colunas (0 a 7)
            alien = Alien(alien_positions[x], y)
            all_sprites.add(alien)
            aliens.add(alien)
    
    return pygame.time.get_ticks()

def restart_game(running, reset):

         
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            reset = False

        
        elif event.type == pygame.QUIT:
            running = False
            reset = False

    
    return running, reset



pygame.init()


pygame.mixer.init()

# Som de explosão
death = pygame.mixer.Sound('Explosion.mp3')
death.set_volume(0.05) 



# Screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Space Invaders')
clock = pygame.time.Clock()
running = True

# Imagens
background = pygame.image.load('SpaceBK.jpg')# Imagem de fundo
background = pygame.transform.scale(background, (800, 600))
life_image = pygame.image.load('Life.png')  # Imagem de vida
life_image = pygame.transform.scale(life_image, (30, 22)) 

# Sprites and groups
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
aliens = pygame.sprite.Group()
start_time = create_alien(True)
alien_bullets = pygame.sprite.Group()

# Cria o player
player = Player()
all_sprites.add(player)

# Variáveis de verificação
dead_aliens = 0
life = 3



# Fonte para exibir o tempo
font = pygame.font.Font(None, 36)



while running:
    # Obejtos de verificações mutáveis
    
    AlienBullet_collided = pygame.sprite.spritecollideany(player, alien_bullets)
  
    reset = True # Variável para esperar o restart
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill('white')

    # Detect collisions between bullets and aliens
    bullet_collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    for bullet in bullet_collisions:
        for alien in bullet_collisions[bullet]:
            dead_aliens += 1

    # Detect collisions between aliens
    alien_collisions = pygame.sprite.groupcollide(aliens, aliens, False, False)
    for alien in alien_collisions:
        if len(alien_collisions[alien]) > 1:  # Se houver mais de um alien na colisão
            alien.on_collision()
    
    if pygame.sprite.spritecollideany(player, aliens) or life == 0:
        print("Colisão detectada entre o player e um alien!")
        reset = True
        while reset:
            show_collision_animation(screen, screen_width, screen_height)
            running, reset = restart_game(running, reset)
        
        if reset == None:
            running = False
            
        start_time = create_alien(True) 

        life = 3

        dead_aliens = 0
    # Declaração de colisão entre player e alien
    if AlienBullet_collided:
        print("Colisão detectada entre o player e um alien!")
        AlienBullet_collided.kill()
        pygame.mixer.Sound.play(death)
        life -= 1


    # Calcula o tempo decorrido
    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000  # Converte para segundos
    
    for alien in aliens:
        if random.random() < 0.001:  # 0.1% de chance de atirar a cada frame
            alien.shoot()


    # Exibe o tempo na tela
    time_text = font.render(f"Tempo: {elapsed_time:.2f}s", True, (0, 0, 0))


    
    
    # Desenha coisa na tela
    screen.blit(time_text, (10, 10))
    screen.blit(background, (0, 0))

    for i in range(life):
       
        screen.blit(life_image, (10 + i * 40, 570))
      

    

    # Update and draw all sprites
    all_sprites.update(elapsed_time, dead_aliens)
    all_sprites.draw(screen)

    #Aumenta velocidade X dos aliens
    if dead_aliens  == 8:
        dead_aliens = 0

    # print(f"Elapsed time: {elapsed_time:.2f}s Start time {start_time} Last time {pygame.time.get_ticks()}")
    pygame.display.flip()
    clock.tick(60)  # 60 frames per second
pygame.quit()