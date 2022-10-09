import pygame
import random 
from pygame.locals import *
pygame.init()

running = True
lepercon = pygame.image.load("L.png")
coin = pygame.image.load("coin.png")
lepercon = pygame.transform.scale(lepercon,(100,100))
screen = pygame.display.set_mode((1000, 1000))
player_x =  0
player_y = 900
pygame.font.init()
coin_on_screen = []
backround1 = pygame.image.load("backround1.png")
score = 0
backround1 = pygame.transform.scale(backround1,(1000,1000))
backround2 = pygame.image.load("backround2.png")
backround2 = pygame.transform.scale(backround2,(1000,1000))
heart = pygame.image.load("heart.png")
curr_backround = backround1
dark_coin = pygame.image.load("dark_coin.png")
screen = pygame.display.set_mode((1000, 1000))
player_hitbox = (player_x, player_y, 80, 100)
player_rect = pygame.Rect(player_hitbox)
smallfont = pygame.font.Font(None, 30)
bigfont = pygame.font.Font(None, 75)
high_score = 0
amt_heart = 3

clock = pygame.time.Clock()
heart = pygame.transform.scale(heart,(100,50))
you_died = False
class coin:
    def __init__(self, x, y, kills, pic, is_heart):
        self.x = x
        self.y = y
        self.is_heart = is_heart
        self.kills = kills
        self.heart = pygame.image.load("heart.png")
        self.image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(self.image,(100,100))
        self.dark_image = pygame.image.load("dark_coin.png")
        self.heart = pygame.transform.scale(self.heart,(100,50))
        self.dark_image = pygame.transform.scale(self.dark_image,(100,100))
        self.hitbox = (self.x, self.y, 100, 100)
        self.rect_box = pygame.Rect(self.hitbox)
    def display(self, screen):
        self.hitbox = (self.x, self.y, 100, 100)
        self.rect_box = pygame.Rect(self.hitbox)
        if self.kills == True and self.is_heart == False :
            screen.blit(self.dark_image, (self.x, self.y))
        if self.is_heart == True and self.kills == False:
            screen.blit(self.heart, (self.x, self.y))
        if self.kills == False and self.is_heart == False:
            screen.blit(self.image, (self.x, self.y))

        #pygame.draw.rect(screen, (0, 0, 0), self.rect_box, 2)
    def move(self):
        self.y += 15
    def get_hitbox(self):
        return self.rect_box
    def get_kills(self):
        return self.kills
    def get_is_heart(self):
        return self.is_heart
    def get_y(self):
        return self.y
def display_text():
    score_text = smallfont.render("score " +str(score), False, "black")
    h_score_text = smallfont.render("high score " +str(high_score), False, "black")
    screen.blit(score_text, [0,0])
    screen.blit(h_score_text, [150,0])
def died():
    death = bigfont.render("you died :(", False, "black")
    press_space = bigfont.render("press space to restart", False, "black")
    screen.blit(death, [500,500])
    screen.blit(press_space, [300,400])
def collsion():
    for i in coin_on_screen:
        if i.get_hitbox().colliderect(player_rect) and i.get_kills() == False and i.get_is_heart() == False:
            coin_on_screen.remove(i)
            return True
        if i.get_hitbox().colliderect(player_rect) and i.get_kills() == True and i.get_is_heart() == False:
            coin_on_screen.remove(i)
            return False
        else:
            pass
def collsion_with_heart():
    for i in coin_on_screen:
        if i.get_hitbox().colliderect(player_rect) and i.get_kills() == False and i.get_is_heart() == True:
            coin_on_screen.remove(i)
            return True
        else:
            pass

while running == True:
    clock.tick(60)
    screen = pygame.display.set_mode((1000, 1000))
    screen.fill((255,255,255))
    screen.blit(curr_backround, (1,1))


    #this closes the game when you hit the x
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    if score >= 30:
        curr_backround = backround2
    spwan_coin = random.randint(1, 100)

    if spwan_coin == 2 and you_died == False:
        where_coin_spwan_x = random.randint(1, 900)
        where_coin_spwan_y = 0
        is_dark = random.randint(1, 3)
        is_heart = random.randint(1, 5)
        if is_dark == 1 and is_heart != 5:
            coin_on_screen.append(coin(where_coin_spwan_x, where_coin_spwan_y, True, dark_coin, False))
        if is_dark!=1 and is_heart != 5:
            coin_on_screen.append(coin(where_coin_spwan_x, where_coin_spwan_y, False, coin, False))
        if is_heart == 5 and is_dark != 1:
            coin_on_screen.append(coin(where_coin_spwan_x, where_coin_spwan_y, False, coin, True))
    for i in coin_on_screen:
        i.display(screen)
        i.move()
        if i.get_y() >= 1000 and i.get_kills() == False and i.get_is_heart() == False:
            amt_heart-=1
            coin_on_screen.remove(i)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and you_died == False: 
        player_x-= 15
    if keys[pygame.K_d] and you_died == False:
        player_x+= 15
    display_text()
    collsion_output = collsion()
    if collsion_output == True and you_died == False:
        score +=1
    if collsion_output == False and you_died == False:
        amt_heart -= 1
    if you_died == True:
        print("test 2")
        died()
        amt_heart = 3
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            you_died = False
        if score > high_score:
            high_score = score
        score = 0


        coin_on_screen = []
    if collsion_with_heart() == True and amt_heart !=3:
        amt_heart += 1 
    player_hitbox = (player_x, player_y, 85, 80)
    player_rect = pygame.Rect(player_hitbox)
    #pygame.draw.rect(screen, (0, 0, 0), player_hitbox, 1)
    screen.blit(lepercon, (player_x, player_y))

    if amt_heart == 3:

        screen.blit(heart, (700, 0))
        screen.blit(heart, (800, 0))
        screen.blit(heart, (900, 0))
    elif amt_heart == 2:
        screen.blit(heart, (800, 0))
        screen.blit(heart, (900, 0))
    if amt_heart == 1:
        screen.blit(heart, (900, 0))
    if amt_heart == 0:
        you_died = True
    if player_x >= 950:
        player_x  -= 15
    if player_x <= -60:
        player_x  += 15
 
    pygame.display.update()
pygame.quit()
