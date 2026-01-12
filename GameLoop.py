# Example file showing a circle moving on screen
import pygame
from random import randint

# pygame setup
pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_vel = 0.0
screen_vel = 200
screen_pos = 0.0

hindernisse = []
offset = 0
for i in range (4):
    hindernisse.append([randint(100, 400), offset])
    offset += 200

  


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("blue")

    for h in hindernisse:
        gap = h[0]
        pos = h[1]
        pygame.draw.rect(screen, "green", pygame.Rect(pos, 0, 50, gap))
        pygame.draw.rect(screen, "green", pygame.Rect(pos, gap + 100, 50, 500))
        if pos < -50:
            hindernisse.remove(h)
            new_gap = randint(100, 400)
            new_pos = hindernisse[-1][1] + 200
            hindernisse.append([new_gap, new_pos])

    pygame.draw.rect(screen, "green", pygame.Rect(screen_pos, 0, 50, gap1))
    pygame.draw.rect(screen, "green", pygame.Rect(screen_pos, gap1 + 100, 50, 200))

    pygame.draw.rect(screen, "green", pygame.Rect(screen_pos + 200, 0, 50, gap2))
    pygame.draw.rect(screen, "green", pygame.Rect(screen_pos + 200, gap2 + 100, 50, 200))

    pygame.draw.rect(screen, "green", pygame.Rect(screen_pos + 400, 0, 50, gap3))
    pygame.draw.rect(screen, "green", pygame.Rect(screen_pos + 400, gap3 + 100, 50, 200))

    pygame.draw.rect(screen, "green", pygame.Rect(screen_pos + 600, 0, 50, gap4))
    pygame.draw.rect(screen, "green", pygame.Rect(screen_pos + 600, gap4 + 100, 50, 200))

    screen_pos -= screen_vel * dt

    pygame.draw.circle(screen, "red", player_pos, 20)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        player_pos.y -= 300 * dt
        player_vel = -300

    else: player_pos.y += player_vel * dt

    player_vel += 500 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()