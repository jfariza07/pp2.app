#lab8.1


import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Coin Collection")

WHITE = (255, 255, 255)
YELLOW = (255, 223, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

player_size = 50
player_x, player_y = WIDTH // 2, HEIGHT - 100
player_speed = 5

coin_radius = 20
coin_x = random.randint(coin_radius, WIDTH - coin_radius)
coin_y = random.randint(coin_radius, HEIGHT - 200)

score = 0
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < HEIGHT - player_size:
        player_y += player_speed
    
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    coin_center = (coin_x, coin_y)
    distance = math.sqrt((player_rect.centerx - coin_center[0])**2 + 
                         (player_rect.centery - coin_center[1])**2)
    
    if distance < coin_radius + player_size/2:
        score += 1
        while True:
            coin_x = random.randint(coin_radius, WIDTH - coin_radius)
            coin_y = random.randint(coin_radius, HEIGHT - 200)
            new_distance = math.sqrt((player_rect.centerx - coin_x)**2 + 
                                    (player_rect.centery - coin_y)**2)
            if new_distance > coin_radius + player_size:
                break

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, player_rect)
    pygame.draw.circle(screen, YELLOW, coin_center, coin_radius)
    
    score_surface = font.render(f"Coins: {score}", True, BLACK)
    score_rect = score_surface.get_rect(topright=(WIDTH - 20, 20))
    bg_rect = score_rect.inflate(20, 10)
    pygame.draw.rect(screen, (200, 200, 200, 128), bg_rect, 0, 5)
    screen.blit(score_surface, score_rect)
    
    pygame.display.update()

pygame.quit()


#lab8.2
import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
INITIAL_SPEED = 10
SPEED_INCREMENT = 1
FOOD_PER_LEVEL = 3

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GAME_OVER_COLOR = (200, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
font = pygame.font.Font(None, 36)

def generate_food(snake):
    while True:
        food_x = random.randint(1, GRID_WIDTH - 2) * GRID_SIZE
        food_y = random.randint(1, GRID_HEIGHT - 2) * GRID_SIZE
        food_pos = (food_x, food_y)
        
        if food_pos not in snake:
            return food_pos

def draw_game(snake, food, score, level):
    screen.fill(WHITE)
    
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, GRID_SIZE, GRID_SIZE))
    
    pygame.draw.rect(screen, RED, (*food, GRID_SIZE, GRID_SIZE))
    
    score_text = font.render(f"Score: {score}", True, BLACK)
    level_text = font.render(f"Level: {level}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))
    
    pygame.display.update()

def game_over_screen(score, level):
    screen.fill(WHITE)
    
    game_over_text = font.render("GAME OVER", True, GAME_OVER_COLOR)
    final_score = font.render(f"Final Score: {score}", True, BLACK)
    final_level = font.render(f"Final Level: {level}", True, BLACK)
    restart_text = font.render("Press R to restart", True, BLACK)
    quit_text = font.render("Press Q to quit", True, BLACK)
    
    screen.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//2 - 60))
    screen.blit(final_score, (WIDTH//2 - final_score.get_width()//2, HEIGHT//2 - 20))
    screen.blit(final_level, (WIDTH//2 - final_level.get_width()//2, HEIGHT//2 + 20))
    screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, HEIGHT//2 + 60))
    screen.blit(quit_text, (WIDTH//2 - quit_text.get_width()//2, HEIGHT//2 + 100))
    
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

def main():
    snake = [(100, 100), (80, 100), (60, 100)]
    snake_dir = (GRID_SIZE, 0)
    score = 0
    level = 1
    speed = INITIAL_SPEED
    food = generate_food(snake)
    
    clock = pygame.time.Clock()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and snake_dir != (GRID_SIZE, 0):
            snake_dir = (-GRID_SIZE, 0)
        if keys[pygame.K_RIGHT] and snake_dir != (-GRID_SIZE, 0):
            snake_dir = (GRID_SIZE, 0)
        if keys[pygame.K_UP] and snake_dir != (0, GRID_SIZE):
            snake_dir = (0, -GRID_SIZE)
        if keys[pygame.K_DOWN] and snake_dir != (0, -GRID_SIZE):
            snake_dir = (0, GRID_SIZE)
        
        new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
        if (new_head[0] < 0 or new_head[0] >= WIDTH or 
            new_head[1] < 0 or new_head[1] >= HEIGHT):
            if game_over_screen(score, level):
                return main()
            else:
                return
        
        if new_head in snake:
            if game_over_screen(score, level):
                return main()
            else:
                return
        
        snake.insert(0, new_head)
        
        if new_head == food:
            score += 1
            if score % FOOD_PER_LEVEL == 0:
                level += 1
                speed += SPEED_INCREMENT
            
            food = generate_food(snake)
        else:
            snake.pop()
        
        draw_game(snake, food, score, level)
        clock.tick(speed)
    
    pygame.quit()

if __name__ == "__main__":
    main()


#lab8.3
import pygame
import pygame.gfxdraw

pygame.init()

WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Drawing Tool")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)
GRAY = (200, 200, 200)

colors = [BLACK, RED, GREEN, BLUE, YELLOW, PURPLE, CYAN]
color_names = ["Black", "Red", "Green", "Blue", "Yellow", "Purple", "Cyan"]
color_index = 0

drawing = False
last_pos = None
current_mode = "pen"
brush_size = 5
fill_mode = False

font_small = pygame.font.SysFont('Arial', 14)
font_large = pygame.font.SysFont('Arial', 24)

toolbar = pygame.Surface((WIDTH, 50))
toolbar.fill(GRAY)

screen.fill(WHITE)
clock = pygame.time.Clock()

def draw_color_buttons():
    """Draw color selection buttons"""
    for i, color in enumerate(colors):
        pygame.draw.rect(toolbar, color, (10 + i*40, 10, 30, 30))
        if i == color_index:
            pygame.draw.rect(toolbar, WHITE, (10 + i*40, 10, 30, 30), 2)

def draw_mode_buttons():
    """Draw mode selection buttons"""
    modes = [("Pen", "p"), ("Rect", "r"), ("Circle", "c"), ("Eraser", "e"), ("Fill", "f")]
    for i, (name, key) in enumerate(modes):
        active = (current_mode == name.lower()) or (current_mode == "pen" and name == "Pen") or (fill_mode and name == "Fill")
        btn_color = WHITE if active else GRAY
        pygame.draw.rect(toolbar, btn_color, (300 + i*80, 10, 70, 30))
        text = font_small.render(name, True, BLACK)
        toolbar.blit(text, (300 + i*80 + 35 - text.get_width()//2, 20))

def draw_brush_size():
    """Draw brush size controls"""
    pygame.draw.rect(toolbar, WHITE, (700, 10, 200, 30))
    text = font_small.render(f"Size: {brush_size}", True, BLACK)
    toolbar.blit(text, (700 + 10, 20))
    pygame.draw.rect(toolbar, WHITE, (700 + 120, 10, 30, 30))
    pygame.draw.rect(toolbar, WHITE, (700 + 160, 10, 30, 30))
    plus = font_small.render("+", True, BLACK)
    minus = font_small.render("-", True, BLACK)
    toolbar.blit(plus, (700 + 135 - plus.get_width()//2, 20))
    toolbar.blit(minus, (700 + 175 - minus.get_width()//2, 20))

def draw_ui():
    """Draw the entire user interface"""
    screen.blit(toolbar, (0, 0))
    
    draw_color_buttons()
    draw_mode_buttons()
    draw_brush_size()
    
    color_text = font_small.render(f"Color: {color_names[color_index]}", True, BLACK)
    screen.blit(color_text, (10, HEIGHT - 30))

def handle_mouse_down(pos):
    """Handle mouse button down events"""
    global drawing, last_pos, rect_start, circle_start

    if pos[1] < 50:
        for i in range(len(colors)):
            if 10 + i*40 <= pos[0] <= 40 + i*40 and 10 <= pos[1] <= 40:
                return "color_change", i
        
        modes = ["pen", "rect", "circle", "eraser", "fill"]
        for i in range(5):
            if 300 + i*80 <= pos[0] <= 370 + i*80 and 10 <= pos[1] <= 40:
                if i == 4:
                    return "fill_toggle", None
                return "mode_change", modes[i]
        
        if 700 + 120 <= pos[0] <= 730 + 120 and 10 <= pos[1] <= 40:
            return "size_change", 1
        if 700 + 160 <= pos[0] <= 730 + 160 and 10 <= pos[1] <= 40:
            return "size_change", -1
        
        return None, None
    
    drawing = True
    last_pos = pos
    
    if current_mode == "rect":
        rect_start = pos
    elif current_mode == "circle":
        circle_start = pos
    
    return None, None

def draw_on_canvas(current_pos):
    """Handle drawing based on current mode"""
    if current_mode == "pen":
        if last_pos:
            pygame.draw.line(screen, colors[color_index], last_pos, current_pos, brush_size)
        return current_pos
    
    elif current_mode == "eraser":
        pygame.draw.circle(screen, WHITE, current_pos, brush_size * 2)
        return last_pos
    
    elif current_mode == "rect":
        temp_surface = screen.copy()
        temp_surface.blit(screen, (0, 0))
        width = current_pos[0] - rect_start[0]
        height = current_pos[1] - rect_start[1]
        
        if fill_mode:
            pygame.draw.rect(temp_surface, colors[color_index], (rect_start[0], rect_start[1], width, height))
        else:
            pygame.draw.rect(temp_surface, colors[color_index], (rect_start[0], rect_start[1], width, height), brush_size)
        
        screen.blit(temp_surface, (0, 0))
        return last_pos
    
    elif current_mode == "circle":
        temp_surface = screen.copy()
        temp_surface.blit(screen, (0, 0))
        radius = int(((current_pos[0] - circle_start[0])**2 + (current_pos[1] - circle_start[1])**2)**0.5)
        
        if fill_mode:
            pygame.draw.circle(temp_surface, colors[color_index], circle_start, radius)
        else:
            pygame.draw.circle(temp_surface, colors[color_index], circle_start, radius, brush_size)
        
        screen.blit(temp_surface, (0, 0))
        return last_pos
    
    return last_pos

def finalize_shape(end_pos):
    if current_mode == "rect":
        width = end_pos[0] - rect_start[0]
        height = end_pos[1] - rect_start[1]
        
        if fill_mode:
            pygame.draw.rect(screen, colors[color_index], (rect_start[0], rect_start[1], width, height))
        else:
            pygame.draw.rect(screen, colors[color_index], (rect_start[0], rect_start[1], width, height), brush_size)
    
    elif current_mode == "circle":
        radius = int(((end_pos[0] - circle_start[0])**2 + (end_pos[1] - circle_start[1])**2)**0.5)
        
        if fill_mode:
            pygame.draw.circle(screen, colors[color_index], circle_start, radius)
        else:
            pygame.draw.circle(screen, colors[color_index], circle_start, radius, brush_size)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            action, value = handle_mouse_down(event.pos)
            
            if action == "color_change":
                color_index = value
            elif action == "mode_change":
                current_mode = value
                fill_mode = False
            elif action == "fill_toggle":
                fill_mode = not fill_mode
            elif action == "size_change":
                brush_size = max(1, min(50, brush_size + value))
        
        elif event.type == pygame.MOUSEBUTTONUP:
            if drawing and current_mode in ["rect", "circle"]:
                finalize_shape(event.pos)
            drawing = False
            last_pos = None
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                screen.fill(WHITE)
            elif event.key == pygame.K_s:
                pass
    if drawing and pygame.mouse.get_pressed()[0]:
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[1] > 50:
            last_pos = draw_on_canvas(mouse_pos)
    
    draw_ui()
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()