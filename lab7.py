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