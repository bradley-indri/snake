import pygame
from food import Food
from snake import * 

# Game loop
pygame.init()
window = pygame.display.set_mode((300,300))
pygame.display.set_caption("Snek gmae")
block_size = 20
snek = Snake(block_size)
food = Food(block_size,(window.get_width(), window.get_height()))

run = True
while run:
  pygame.time.delay(100)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    snek.steer(Direction.LEFT)
  elif keys[pygame.K_RIGHT]:
    snek.steer(Direction.RIGHT)
  elif keys[pygame.K_UP]:
    snek.steer(Direction.UP)
  elif keys[pygame.K_DOWN]:
    snek.steer(Direction.DOWN)
  elif keys[pygame.K_SPACE]:
    snek.eat()

  snek.move()
  snek.check_for_food(food)
  window.fill((0,0,0))
  snek.draw(pygame, window)
  food.draw(pygame, window)
  pygame.display.update()
# end while loop

pygame.quit()