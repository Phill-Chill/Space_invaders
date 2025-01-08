import pygame
import time
import random
from Player import Ship, Ship2
from Config import screen_width, screen_height
from Aliens import Alien
from Sprites import all_sprites , bullets,  aliens, alien_bullets
import json ,os,sys
from Method import _Method
from Menu import Menu

class Game:
   


    pygame.init()

    pygame.mixer.init()

    # Som de explosão
    death = pygame.mixer.Sound('Explosion.mp3')
    death.set_volume(0.05) 

    # Screen
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Space Invaders')
    clock = pygame.time.Clock()
    running = True

    # Imagens
    background = pygame.image.load('SpaceBK.jpg')# Imagem de fundo
    background = pygame.transform.scale(background, (800, 600))
    life_image = pygame.image.load('Life.png')  # Imagem de vida
    life_image = pygame.transform.scale(life_image, (30, 22)) 

    

    # Cria o player
    player = Ship()
    
    all_sprites.add(player)
    

    # Variáveis de verificação
    dead_aliens = 0
    life = 3
    user_points = 0
    method = _Method()
    max_points = method.load_points()
    phase_reset = False
    reset = True
    
    start_time = method.create_alien(True)

    def start_game(screen, clock): 
        menu = Menu()
        game_state = 'menu'
        player2 = None
        while game_state == 'menu':
            action = menu.handle_events()

            if action == '1play':
                game_state = 'playing'
            elif action == '2play': 
                game_state = '2play'
                player2 = Ship2()
                all_sprites.add(player2)
            elif action == 'exit':
                pygame.quit()
                sys.exit()
            menu.draw(screen)
            pygame.display.flip()
            clock.tick(60)
            
        return game_state, player2

    action, player2 = start_game(screen, clock)
    
    while running:
        
        # Obejtos de verificações mutáveis

        AlienBullet_collided = pygame.sprite.spritecollideany(player, alien_bullets)
        

        AlienBullet_collided2 = pygame.sprite.spritecollideany(player2, alien_bullets) if player2 else None

        reset = True # Variável para esperar o restart

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        

        # Detect collisions between bullets and aliens
        bullet_collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
        for bullet in bullet_collisions:
            for alien in bullet_collisions[bullet]:
                dead_aliens += 1
                user_points += 10

        # Detect collisions between aliens
        alien_collisions = pygame.sprite.groupcollide(aliens, aliens, False, False)
        for alien in alien_collisions:
            if len(alien_collisions[alien]) > 1:  # Se houver mais de um alien na colisão
                alien.on_collision()

        if pygame.sprite.spritecollideany(player, aliens) or life == 0:
            
            life = 0
            reset = True
            while reset:
                method.show_collision_animation(screen, screen_width, screen_height)
                running, reset = method.restart_game(running, reset)             
                user_points = 0   

            start_time = method.create_alien(True)
            life = 3
            action = 'menu'
            running = False
            
            

            dead_aliens = 0
        # Declaração de colisão entre player e alien
        if AlienBullet_collided or AlienBullet_collided2:
                   
            pygame.mixer.Sound.play(death)
            life -= 1

            if AlienBullet_collided2:
                AlienBullet_collided2.kill()
            else:
                AlienBullet_collided.kill()


        if user_points > max_points:
            max_points = user_points
            method.save_points(max_points)
            max_points = method.load_points()

       
        phase_reset = method.restart_phase(dead_aliens,running, reset, life)
        if phase_reset:         
            dead_aliens = 0
            start_time = method.create_alien(True)
 
        
        
    

        # Calcula o tempo decorrido
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000  # Converte para segundos

        for alien in aliens:
            if random.random() < 0.001:  # 0.1% de chance de atirar a cada frame
                alien.shoot()


        font = pygame.font.Font('PressStart2P.ttf', 10)

        points_max = font.render(f"Max points: {max_points}", True, (255, 255, 255))
        points_user = font.render(f"Points: {user_points}", True, (255, 255, 255))

        # Desenha coisa na tela
        screen.blit(background, (0, 0))
        screen.blit(points_max, (10, 530))
        screen.blit(points_user, (10, 550))
        for i in range(life):
        
            screen.blit(life_image, (10 + i * 40, 570))




        # Update and draw all sprites
        all_sprites.update(elapsed_time, dead_aliens)
        all_sprites.draw(screen)

       
        if dead_aliens  == 40:
             dead_aliens = 0

        if action == 'menu' and player2:
            player2.kill()
            player2 = None
        
        

        # print(f"Elapsed time: {elapsed_time:.2f}s Start time {start_time} Last time {pygame.time.get_ticks()}")
        pygame.display.flip()
        clock.tick(60)  # 60 frames per second

        if not running:
            action , player2 = start_game(screen, clock)
            running = True
    pygame.quit()