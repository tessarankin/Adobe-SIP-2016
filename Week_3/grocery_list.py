import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)
colors = [BLACK, GREEN, BLUE, RED]
 
def random_color():
  return random.choice(colors)

pygame.init()
 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
 
class Building():
  def __init__(self, x_point, y_point, width, height, color):
    self.x_point= x_point
    self.y_point= y_point
    self.width= width
    self.height= height
    self.color= color

  def draw(self):
    pygame.draw.rect(screen, self.color, (self.x_point, SCREEN_HEIGHT - self.height, self.width, self.height))

  def move(self, speed):
    self.x_point += speed

class Scroller(object):
  
  def __init__(self, width, height, base, color, speed):
    self.width= width
    self.height= height
    self.base= base
    self.color= color
    self.speed= speed
    self.building_list= []
    self.add_buildings()
    
  def add_buildings(self):
    self.add_building(-100,100)
    random_width = 0
    x_location=0
    while x_location<= self.width:
      random_width = random.randint(50, 500)
      self.add_building(x_location, random_width)
      x_location = x_location + random_width
 
  def add_building(self, x_location, combined_width):
    building1 = Building(x_location, self.base, combined_width, random.randint(50, 800), random_color())
    self.building_list.append(building1)

  def draw_buildings(self):
    pygame.draw.rect(screen, self.color, (0, SCREEN_HEIGHT, self.width, SCREEN_HEIGHT - self.height))
    for building1 in self.building_list:
      building1.draw()

  def move_buildings(self):
    for building1 in self.building_list:
      building1.move(self.speed)
      

FRONT_SCROLLER_COLOR = (0,0,30)
MIDDLE_SCROLLER_COLOR = (30,30,100)
BACK_SCROLLER_COLOR = (50,50,150)
BACKGROUND_COLOR = (17, 9, 89)
 
front_scroller = Scroller(SCREEN_WIDTH, 500, 0, FRONT_SCROLLER_COLOR, 3)
middle_scroller = Scroller(SCREEN_WIDTH, 300, 100, MIDDLE_SCROLLER_COLOR, 2)
back_scroller = Scroller(SCREEN_WIDTH, 400, 200, BACK_SCROLLER_COLOR, 1)

pygame.display.set_caption("CityScroller") 
clock = pygame.time.Clock() 
done = False
while not done:
   for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
   screen.fill(BACKGROUND_COLOR)
 
   back_scroller.draw_buildings()
   back_scoller.move_buildings()
   middle_scroller.draw_buildings()
   middle_scoller.move_buildings()
   front_scroller.draw_buildings()
   front_scroller.move_buildings()

   pygame.display.flip()
 
   clock.tick(60)

pygame.quit()