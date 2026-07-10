import pygame
import random
import sys

pygame.init()

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
GRID_SIZE = 20
FPS = 10

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

def spawn_food():
    return [random.randint(0, (WINDOW_WIDTH-GRID_SIZE)//GRID_SIZE)*GRID_SIZE,
            random.randint(0, (WINDOW_HEIGHT-GRID_SIZE)//GRID_SIZE)*GRID_SIZE]

snake = [[WINDOW_WIDTH//2, WINDOW_HEIGHT//2]]
food = spawn_food()
direction = [GRID_SIZE, 0]
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction[1] == 0:
                direction = [0, -GRID_SIZE]
            if event.key == pygame.K_DOWN and direction[1] == 0:
                direction = [0, GRID_SIZE]
            if event.key == pygame.K_LEFT and direction[0] == 0:
                direction = [-GRID_SIZE, 0]
            if event.key == pygame.K_RIGHT and direction[0] == 0:
                direction = [GRID_SIZE, 0]
    
    head = [snake[0][0]+direction[0], snake[0][1]+direction[1]]
    
    if head in snake[1:] or head[0]<0 or head[0]>=WINDOW_WIDTH or head[1]<0 or head[1]>=WINDOW_HEIGHT:
        game_over = True
    
    snake.insert(0, head)
    
    if head == food:
        food = spawn_food()
    else:
        snake.pop()
    
    screen.fill(BLACK)
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))
    pygame.draw.rect(screen, RED, (food[0], food[1], GRID_SIZE, GRID_SIZE))
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
