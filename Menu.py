import pygame
import sys
from Config import screen_width, screen_height

class Menu:
    def __init__(self):
        # Carrega e redimensiona o fundo do menu
        self.background = pygame.image.load("assets/Menu.jpg").convert()
        self.background = pygame.transform.scale(self.background, (screen_width, screen_height))
        
        # Carrega e redimensiona a imagem do título
        self.title_image = pygame.image.load("assets/Title.png").convert_alpha()
        self.title_image = pygame.transform.scale(self.title_image, (500, 500))
        
        # Define a fonte para o texto dos botões
        self.font = pygame.font.Font('assets/PressStart2P.ttf', 50)  
        
        # Lista de botões do menu com o texto e a ação correspondente
        self.buttons = [
            {"text": "1 Player", "action": "1play"},
            {"text": "2 Players", "action": "2play"},
            {"text": "Sair", "action": "exit"},
        ]
        
        # Define a altura do botão e o espaçamento entre os botões
        self.button_height = 60
        self.button_spacing = 20

    def draw_button(self, screen, text, y_position, hover = False):
        """Desenha um botão no menu na posição vertical especificada."""
        
        # Cria um retângulo para o botão com largura fixa e altura definida
        button_rect = pygame.Rect(
            screen_width // 2 - 100, y_position, 200, self.button_height
        )
        
        text_surface = self.font.render(text, True, (94, 94, 94))
        
        if hover:
             text_surface = self.font.render(text, True, (255,255,255)) 
        # Desenha o fundo branco do botão
        # pygame.draw.rect(screen, (255, 255, 255), button_rect)
        
        # Desenha a borda preta do botão
        # pygame.draw.rect(screen, (0, 0, 0), button_rect, 3)

        # Renderiza o texto do botão
        
        
        # Posiciona o texto no centro do botão
        screen.blit(
            text_surface,
            (screen_width // 2 - text_surface.get_width() // 2, y_position + 15)
        )
    
    def draw(self, screen):
        """Desenha todos os elementos do menu (fundo, título e botões)."""
        
        # Desenha o fundo
        screen.blit(self.background, (0, 0))
        
        # Desenha a imagem do título, centralizando ela na tela
        screen.blit(
            self.title_image, 
            (screen_width // 2 - self.title_image.get_width() // 2, -60)
        )
        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for index, button in enumerate(self.buttons):
            y_position = 300 + index * (self.button_height + self.button_spacing)
            button_rect = pygame.Rect(
                screen_width // 2 - 100, y_position, 200, self.button_height
            )
            hover = button_rect.collidepoint(mouse_x, mouse_y)
            self.draw_button(screen, button["text"], y_position, hover)

    def handle_events(self):
        """Lida com os eventos do menu, como cliques nos botões."""
       
        # Verifica todos os eventos do pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Fecha o jogo se a janela for fechada
                sys.exit()

            # Verifica se o evento é um clique com o mouse
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Clique esquerdo do mouse
                    mouse_x, mouse_y = event.pos
                    # Verifica se o clique foi em algum dos botões
                    for index, button in enumerate(self.buttons):
                        y = 300 + index * (self.button_height + self.button_spacing)
                        button_rect = pygame.Rect(
                            screen_width // 2 - 100, y, 200, self.button_height
                        )
                        # Verifica se o clique ocorreu dentro da área do botão
                        if button_rect.collidepoint(mouse_x, mouse_y):
                            return button["action"]  # Retorna a ação do botão clicado
        
        return None