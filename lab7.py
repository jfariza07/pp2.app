lab7.1

import pygame
import time
import math
from datetime import datetime

pygame.init()

width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mickey Mouse Clock")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

def create_mickey():
    mickey = pygame.Surface((width, height), pygame.SRCALPHA)
    
    pygame.draw.circle(mickey, BLACK, (width//2, height//2), 150)
    
    pygame.draw.circle(mickey, BLACK, (width//2 - 90, height//2 - 90), 70)
    pygame.draw.circle(mickey, BLACK, (width//2 + 90, height//2 - 90), 70)
    
    pygame.draw.circle(mickey, WHITE, (width//2, height//2), 100)
    
    return mickey

def create_hand(length, thickness, color):
    hand = pygame.Surface((length*2, length*2), pygame.SRCALPHA)
    pygame.draw.line(hand, color, (length, length), (length, length - length), thickness)
    return hand

mickey = create_mickey()
minute_hand = create_hand(80, 6, BLACK)
second_hand = create_hand(100, 3, RED)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    now = datetime.now()
    minutes = now.minute
    seconds = now.second
    
    minute_angle = -math.radians((minutes / 60) * 360 + 90)
    second_angle = -math.radians((seconds / 60) * 360 + 90)
    
    screen.fill(WHITE)
    
    screen.blit(mickey, (0, 0))
    
    rotated_minute = pygame.transform.rotate(minute_hand, math.degrees(minute_angle))
    minute_rect = rotated_minute.get_rect(center=(width//2, height//2))
    screen.blit(rotated_minute, minute_rect.topleft)
    
    rotated_second = pygame.transform.rotate(second_hand, math.degrees(second_angle))
    second_rect = rotated_second.get_rect(center=(width//2, height//2))
    screen.blit(rotated_second, second_rect.topleft)
    
    pygame.display.flip()
    
    clock.tick(30)

pygame.quit()


lab7.2
import pygame
import os
import sys

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Music Player")
font = pygame.font.SysFont('Arial', 24)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

music_dir = "music"
if not os.path.exists(music_dir):
    os.makedirs(music_dir)
    print(f"Created '{music_dir}' directory. Please add some music files there.")
    sys.exit()

playlist = [os.path.join(music_dir, f) for f in os.listdir(music_dir) 
            if f.endswith(('.mp3', '.wav', '.ogg'))]
current_track = 0

KEY_PLAY = pygame.K_p
KEY_STOP = pygame.K_s
KEY_NEXT = pygame.K_RIGHT
KEY_PREV = pygame.K_LEFT

paused = False

def load_track(track_index):
    if 0 <= track_index < len(playlist):
        pygame.mixer.music.load(playlist[track_index])
        pygame.mixer.music.play()
        return track_index
    return current_track

def update_display():
    screen.fill(WHITE)
    
    if playlist:
        track_name = os.path.basename(playlist[current_track])
        text = font.render(f"Now Playing: {track_name}", True, BLACK)
        screen.blit(text, (20, 50))
    
    controls = [
        "Controls:",
        f"Play/Pause: {pygame.key.name(KEY_PLAY).upper()}",
        f"Stop: {pygame.key.name(KEY_STOP).upper()}",
        f"Next: {pygame.key.name(KEY_NEXT)}",
        f"Previous: {pygame.key.name(KEY_PREV)}"
    ]
    
    for i, control in enumerate(controls):
        text = font.render(control, True, BLACK)
        screen.blit(text, (20, 100 + i * 30))
    
    pygame.display.flip()

if playlist:
    current_track = load_track(0)
    update_display()
else:
    print("No music files found in the 'music' directory.")
    sys.exit()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == KEY_PLAY:
                if pygame.mixer.music.get_busy() and not paused:
                    pygame.mixer.music.pause()
                    paused = True
                else:
                    if paused:
                        pygame.mixer.music.unpause()
                        paused = False
                    else:
                        pygame.mixer.music.play()
            
            elif event.key == KEY_STOP:
                pygame.mixer.music.stop()
                paused = False
            
            elif event.key == KEY_NEXT:
                current_track = (current_track + 1) % len(playlist)
                load_track(current_track)
                paused = False
            
            elif event.key == KEY_PREV:
                current_track = (current_track - 1) % len(playlist)
                load_track(current_track)
                paused = False
            
            update_display()
    
    pygame.time.delay(100)

pygame.quit()


lab7.3
import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Movable Red Ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

BALL_RADIUS = 25
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
MOVE_AMOUNT = 20

def draw_ball():
    pygame.draw.circle(screen, RED, (ball_x, ball_y), BALL_RADIUS)

def move_ball(dx, dy):
    global ball_x, ball_y
    if BALL_RADIUS <= ball_x + dx <= WIDTH - BALL_RADIUS:
        ball_x += dx
    if BALL_RADIUS <= ball_y + dy <= HEIGHT - BALL_RADIUS:
        ball_y += dy

def main():
    global ball_x, ball_y
    
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move_ball(0, -MOVE_AMOUNT)
                elif event.key == pygame.K_DOWN:
                    move_ball(0, MOVE_AMOUNT)
                elif event.key == pygame.K_LEFT:
                    move_ball(-MOVE_AMOUNT, 0)
                elif event.key == pygame.K_RIGHT:
                    move_ball(MOVE_AMOUNT, 0)
        
        screen.fill(WHITE)
        draw_ball()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
