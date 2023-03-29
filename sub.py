import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600

# Colors
WHITE = (255, 255, 255)

# Game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Submarine Game")

# Submarine sprite
submarine = pygame.image.load("submarine.png")  # Replace with your 16-bit submarine sprite
submarine_rect = submarine.get_rect()

# Depth charge sprite
depth_charge = pygame.image.load("depth_charge.png")  # Replace with your depth charge sprite
depth_charge_rect = depth_charge.get_rect()

# Game clock
clock = pygame.time.Clock()

# Game loop
running = True
start_time = time.time()
depth_charges = []
drop_interval = 2

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Submarine movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and submarine_rect.left > 0:
        submarine_rect.x -= 5
    if keys[pygame.K_RIGHT] and submarine_rect.right < WIDTH:
        submarine_rect.x += 5
    if keys[pygame.K_UP] and submarine_rect.top > 0:
        submarine_rect.y -= 5
    if keys[pygame.K_DOWN] and submarine_rect.bottom < HEIGHT:
        submarine_rect.y += 5

    # Depth charges
    if time.time() - start_time >= drop_interval:
        start_time = time.time()
        drop_interval = max(0.5, drop_interval * 0.95)  # Increase drop frequency
        new_charge = depth_charge_rect.copy()
        new_charge.x = random.randint(0, WIDTH - depth_charge_rect.width)
        depth_charges.append(new_charge)

    for charge in depth_charges:
        if charge.colliderect(submarine_rect):
            running = False  # Game over
        charge.y += 5
        if charge.top > HEIGHT:
            depth_charges.remove(charge)

    # Drawing
    screen.fill(WHITE)
    screen.blit(submarine, submarine_rect)
    for charge in depth_charges:
        screen.blit(depth_charge, charge)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
