import pygame
from enum import Enum

class Direction(Enum):
  UP = 0
  DOWN = 1
  LEFT = 2
  RIGHT = 3

class Snake:
  length = 3
  direction = Direction.DOWN
  body = [(20,20),(20,40),(20,60)]
  block_size = 20
  color = (255,0,0)

  def __init__(self, block_size):
    self.block_size = block_size

  def move(self):
    curr_head = self.body[-1]
    if self.direction == Direction.DOWN:
      next_head = (curr_head[0], curr_head[1] + self.block_size)
      self.body.append(next_head)
    elif self.direction == Direction.UP:
      next_head = (curr_head[0], curr_head[1] - self.block_size)
      self.body.append(next_head)
    elif self.direction == Direction.RIGHT:
      next_head = (curr_head[0] + self.block_size, curr_head[1])
      self.body.append(next_head)
    elif self.direction == Direction.LEFT:
      next_head = (curr_head[0] - self.block_size, curr_head[1])
      self.body.append(next_head)

    if self.length < len(self.body):
      self.body.pop(0)
  # end move method

  def eat(self):
    self.length += 1

  def draw(self, game):

    for segment in self.body:
      pygame.draw.rect(win, self.color, (segment[0],segment[1],self.block_size, self.block_size))

  def steer(self, direction):
    self.direction = direction


# Game loop

pygame.init()
win = pygame.display.set_mode((800,600))
pygame.display.set_caption("Snek gmae")
block_size = 20
snek = Snake(block_size)


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
  win.fill((0,0,0))
  snek.draw(pygame)
  pygame.display.update()
# end while loop

pygame.quit()