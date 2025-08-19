import pygame, random, sys

pygame.init()
W, H, cell = 400, 400, 20
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

def spawn_food(snake):
    while True:
        x = random.randrange(0, W // cell)
        y = random.randrange(0, H // cell)
        if (x, y) not in snake:
            return (x, y)

snake = [(9, 9)]
direction = (0, 0)
food = spawn_food(snake)
score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1): direction = (0, -1)
            if event.key == pygame.K_DOWN and direction != (0, -1): direction = (0, 1)
            if event.key == pygame.K_LEFT and direction != (1, 0): direction = (-1, 0)
            if event.key == pygame.K_RIGHT and direction != (-1, 0): direction = (1, 0)

    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    # Wall collision
    if head[0] < 0 or head[0] >= W // cell or head[1] < 0 or head[1] >= H // cell:
        print("Game Over! Score:", score)
        pygame.quit(); sys.exit()

    # Self collision
    if head in snake:
        print("Game Over! Score:", score)
        pygame.quit(); sys.exit()

    snake.insert(0, head)
    if head == food:
        score += 1
        food = spawn_food(snake)
    else:
        snake.pop()

    screen.fill((0, 0, 0))
    # Draw food
    pygame.draw.rect(screen, (200, 0, 0), (food[0]*cell, food[1]*cell, cell-1, cell-1))
    # Draw snake
    for i, seg in enumerate(snake):
        color = (0, 255, 0) if i > 0 else (50, 205, 50)
        pygame.draw.rect(screen, color, (seg[0]*cell, seg[1]*cell, cell-1, cell-1))

    txt = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(txt, (10, 10))

    pygame.display.flip()
    clock.tick(10)  # Game speed