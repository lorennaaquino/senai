import pygame
import random
import sys

# Inicialize o Pygame
pygame.init()

# Configurações da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 40

# Crie a tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Jogo da Forca')

# Carregue a fonte
font = pygame.font.Font(None, FONT_SIZE)

# Lista de palavras para o jogo
words = ['python', 'pygame', 'programacao', 'desenvolvimento', 'computador']

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def draw_hangman(wrong_guesses):
    # Função básica para desenhar o esqueleto da forca
    pygame.draw.line(screen, BLACK, (100, 500), (200, 500), 5)  # Base
    pygame.draw.line(screen, BLACK, (150, 500), (150, 100), 5)  # Poste
    pygame.draw.line(screen, BLACK, (150, 100), (250, 100), 5)  # Trave
    pygame.draw.line(screen, BLACK, (250, 100), (250, 150), 5)  # Cordão

    if wrong_guesses > 0:
        pygame.draw.circle(screen, BLACK, (250, 180), 30, 5)  # Cabeça
    if wrong_guesses > 1:
        pygame.draw.line(screen, BLACK, (250, 210), (250, 300), 5)  # Corpo
    if wrong_guesses > 2:
        pygame.draw.line(screen, BLACK, (250, 300), (220, 370), 5)  # Braço esquerdo
    if wrong_guesses > 3:
        pygame.draw.line(screen, BLACK, (250, 300), (280, 370), 5)  # Braço direito
    if wrong_guesses > 4:
        pygame.draw.line(screen, BLACK, (250, 300), (220, 450), 5)  # Perna esquerda
    if wrong_guesses > 5:
        pygame.draw.line(screen, BLACK, (250, 300), (280, 450), 5)  # Perna direita

def main():
    # Escolha uma palavra aleatória
    word = random.choice(words).upper()
    guessed_word = ['_'] * len(word)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong_guesses = 6

    # Loop principal do jogo
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key >= pygame.K_a and event.key <= pygame.K_z:
                    letter = chr(event.key).upper()
                    if letter not in guessed_letters:
                        guessed_letters.append(letter)
                        if letter in word:
                            for i, char in enumerate(word):
                                if char == letter:
                                    guessed_word[i] = letter
                        else:
                            wrong_guesses += 1

        # Atualize a tela
        screen.fill(WHITE)

        # Desenhe a palavra adivinhada
        draw_text(' '.join(guessed_word), font, BLACK, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)

        # Desenhe letras adivinhadas
        draw_text('Letras adivinhadas: ' + ' '.join(guessed_letters), font, BLACK, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)

        # Desenhe o número de tentativas erradas
        draw_text(f'Tentativas erradas: {wrong_guesses}/{max_wrong_guesses}', font, BLACK, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)

        # Desenhe a forca
        draw_hangman(wrong_guesses)

        # Verifique se o jogador perdeu
        if wrong_guesses >= max_wrong_guesses:
            draw_text('Você perdeu! A palavra era: ' + word, font, BLACK, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 200)
            pygame.display.update()
            pygame.time.wait(3000)
            return

        # Verifique se o jogador ganhou
        if ''.join(guessed_word) == word:
            draw_text('Você venceu!', font, BLACK, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 200)
            pygame.display.update()
            pygame.time.wait(3000)
            return

        pygame.display.update()

if __name__ == '__main__':
    main()

