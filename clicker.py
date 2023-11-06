Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pygame
import time
from random import *
pygame.init()
blue = (200, 255 ,255)
mw=pygame.display.set_mode((500,500))
mw.fill(blue)
clock = pygame.time.Clock()
class Area():
  def __init__(self, x = 0 , y = 0 , width=10, height=10, color=None):
      self.rect = pygame.Rect(x , y, width, height)
      self.fill_color = color
  def color(self, new_color):
      self.fill_color = new_color
  def fill(self):
      pygame.draw.rect(mw, self.fill_color, self.rect)
  def outline(self, frame_color, thickness):
      pygame.draw.rect(mw, frame_color, self.rect, thickness)
  def collidepoint(self, x, y):
      return self.rect.collidepoint(x, y)
class Lable(Area):
    def set_text(self,text):
        self.image = pygame.font.SysFont('verdana', 25).render(text, True,(0,0,0))
    def draw(self):
        self.fill()
        mw.blit(self.image,(self.rect.x+10,self.rect.y+10))
yellow=(255,255,0)

cards = []
x = 70
for i in range(4):
    card = Lable(x,170,70,100,yellow)
    card.set_text('click')
    card.outline((0,0,0),4)
    cards.append(card)
    x=x+90
RED = (255, 0, 0)
GREEN = (0, 255, 51)
wait = 0
start_time = time.time()
cur_time = start_time
time_text = Lable(0,0,50,50,blue)
time_text.set_text('Time:')
time_text.draw()
timer = Lable(30,40,50,40,blue)
timer.set_text('0')
timer.draw()
res = Lable(250,0,50,50,blue)
res.set_text('Count:')
res.draw()
b = Lable(320,40,50,40,blue)
b.set_text('0')
b.draw()

points = 0

while True:
    new_time = time.time()
    if new_time - cur_time >= 1:
        timer.set_text(str(int(new_time - start_time)))
        timer.draw()
        cur_time = new_time
    
    
    
    if wait == 0:
        wait = 20
        click = randint(1, 4)
        for i in range(4):
            cards[i].color(yellow)
            if (i + 1) == click:
                cards[i].draw()
            else:
                cards[i].fill()
    else:
        wait-=1
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            for i in range(4):
                if cards[i].collidepoint(x,y):
                    if i + 1 == click:
                        cards[i].color(GREEN)
                        points+=1
                        b.set_text(str(points))
                        b.draw()
                    else:
                        cards[i].color(RED)
                        points-=1
                        b.set_text(str(points))
                        b.draw()
                cards[i].fill()

    
    if points>5:
        win = Lable(0,0,500,500,(0,255,34))
        win.set_text('Win')
        win.fill()
        mw.blit(win.image,(win.rect.x+200,win.rect.y+200))
        break
    if new_time-start_time>11:
        lose = Lable(0,0,500,500,(255,0,0))
        lose.set_text('Lose')
        lose.fill()
        mw.blit(lose.image,(lose.rect.x+200,lose.rect.y+200))
        break

    clock.tick(40)
    pygame.display.update()
pygame.display.update()
