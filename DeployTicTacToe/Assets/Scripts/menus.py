import pygame, sys

# Initialize PyGame
pygame.init()

TEXT_COLOR = (255,255,255)
TEXT_BG_COLOR = (0,0,0)
WIDTH = 512
HEIGHT = 512
BG_COLOR = (20,120,200)



# Initialize Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BG_COLOR)



# class Menus:
#     def __init__(self, player):
#         self.player = player

def is_tied():
    return False




def game_over(player):
    font = pygame.font.Font('freesansbold.ttf', 32)
    text_game_over = font.render('Game Over!', True, TEXT_COLOR, TEXT_BG_COLOR)
    text_rect1 = text_game_over.get_rect()
    text_rect1.center = (WIDTH//2,(HEIGHT//2)-60)

    if is_tied():
        text_won = font.render(f'Tie!', True, TEXT_COLOR, TEXT_BG_COLOR)
    elif player == 1:
        player_n = 'X'
        text_won = font.render(f'{player_n} - Won!', True, TEXT_COLOR, TEXT_BG_COLOR)
    elif player == 2:
        player_n = 'O'
        text_won = font.render(f'{player_n} - Won!', True, TEXT_COLOR, TEXT_BG_COLOR)



    text_rect2 = text_won.get_rect()
    text_rect2.center = (WIDTH//2,HEIGHT//2)


    screen.fill(TEXT_BG_COLOR)
    screen.blit(text_game_over, text_rect1)
    screen.blit(text_won, text_rect2)

game_over(2)

# Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()