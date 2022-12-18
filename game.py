import pygame
from pygame import *
import random
from random import randint
import time
from time import sleep

win = pygame.display.set_mode((1920, 1080), RESIZABLE)
pygame.display.set_caption("Run 'n Gunner")
pygame.font.init()
font = pygame.font.SysFont("Calibri", 100)

bg = pygame.image.load("bg.jpg")
x = 0
y = 0
walk_right = [pygame.image.load("Character/Run__000.png"), pygame.image.load("Character/Run__001.png"), pygame.image.load("Character/Run__002.png"), pygame.image.load("Character/Run__003.png"), pygame.image.load("Character/Run__004.png"), pygame.image.load("Character/Run__005.png"), pygame.image.load("Character/Run__006.png"), pygame.image.load("Character/Run__007.png"), pygame.image.load("Character/Run__008.png"), pygame.image.load("Character/Run__009.png")]

walk_left = [pygame.transform.flip(image, 1, 0) for image in walk_right]

walk_right = [pygame.transform.scale(image, ((int(image.get_width())) // 2, (int(image.get_height())) // 2)) for image in walk_right]

walk_left = [pygame.transform.scale(image, ((int(image.get_width())) // 2, (int(image.get_height())) // 2)) for image in walk_left]

# climb = []
# lose = []

attack_right = [pygame.image.load("Character/Attack__000.png"), pygame.image.load("Character/Attack__001.png"), pygame.image.load("Character/Attack__002.png"), pygame.image.load("Character/Attack__003.png"), pygame.image.load("Character/Attack__004.png"), pygame.image.load("Character/Attack__005.png"), pygame.image.load("Character/Attack__006.png"), pygame.image.load("Character/Attack__007.png"), pygame.image.load("Character/Attack__008.png"), pygame.image.load("Character/Attack__009.png")]

attack_left = [pygame.transform.flip(image, 1, 0) for image in attack_right]

attack_right = [pygame.transform.scale(image, ((int(image.get_width())) // 2, (int(image.get_height())) // 2)) for image in attack_right]

attack_left = [pygame.transform.scale(image, ((int(image.get_width())) // 2, (int(image.get_height())) // 2)) for image in attack_left]

# glide = []
idle_right = [pygame.image.load("Character/Idle__000.png"), pygame.image.load("Character/Idle__001.png"), pygame.image.load("Character/Idle__002.png"), pygame.image.load("Character/Idle__003.png"), pygame.image.load("Character/Idle__004.png"), pygame.image.load("Character/Idle__005.png"), pygame.image.load("Character/Idle__006.png"), pygame.image.load("Character/Idle__007.png"), pygame.image.load("Character/Idle__008.png"), pygame.image.load("Character/Idle__009.png")]

idle_left = [pygame.transform.flip(image, 1, 0) for image in idle_right]

idle_right = [pygame.transform.scale(image, ((int(image.get_width())) // 2, (int(image.get_height())) // 2)) for image in idle_right]

idle_left = [pygame.transform.scale(image, ((int(image.get_width())) // 2, (int(image.get_height())) // 2)) for image in idle_left]

jump_right = [pygame.image.load("Character/Jump__000.png"), pygame.image.load("Character/Jump__001.png"), pygame.image.load("Character/Jump__002.png"), pygame.image.load("Character/Jump__003.png"), pygame.image.load("Character/Jump__004.png"), pygame.image.load("Character/Jump__005.png"), pygame.image.load("Character/Jump__006.png"), pygame.image.load("Character/Jump__007.png"), pygame.image.load("Character/Jump__008.png"), pygame.image.load("Character/Jump__009.png")]

jump_left = [pygame.transform.flip(image, 1, 0) for image in jump_right]

jump_right = [pygame.transform.scale(image, ((int(image.get_width())) // 2, (int(image.get_height())) // 2)) for image in jump_right]

jump_left = [pygame.transform.scale(image, ((int(image.get_width())) // 2, (int(image.get_height())) // 2)) for image in jump_left]

slide_right = [pygame.image.load("Character/Slide__000.png"), pygame.image.load("Character/Slide__001.png"), pygame.image.load("Character/Slide__002.png"), pygame.image.load("Character/Slide__003.png"), pygame.image.load("Character/Slide__004.png"), pygame.image.load("Character/Slide__005.png"), pygame.image.load("Character/Slide__006.png"), pygame.image.load("Character/Slide__007.png"), pygame.image.load("Character/Slide__008.png"), pygame.image.load("Character/Slide__009.png")]

slide_left = [pygame.transform.flip(image, 1, 0) for image in slide_right]

slide_right = [pygame.transform.scale(image, ((int(image.get_width())) // 2, (int(image.get_height())) // 2)) for image in slide_right]

slide_left = [pygame.transform.scale(image, ((int(image.get_width())) // 2, (int(image.get_height())) // 2)) for image in slide_left]

jumping_throw_right = pygame.image.load("Character/Jump_Throw__000.png"), pygame.image.load("Character/Jump_Throw__001.png"), pygame.image.load("Character/Jump_Throw__002.png"), pygame.image.load("Character/Jump_Throw__003.png"), pygame.image.load("Character/Jump_Throw__004.png"), pygame.image.load("Character/Jump_Throw__005.png"), pygame.image.load("Character/Jump_Throw__006.png"), pygame.image.load("Character/Jump_Throw__007.png"), pygame.image.load("Character/Jump_Throw__008.png"), pygame.image.load("Character/Jump_Throw__009.png")

jumping_throw_left = [pygame.transform.flip(image, 1, 0) for image in jumping_throw_right]

jumping_throw_right = [pygame.transform.scale(image, ((int(image.get_width())) // 2, (int(image.get_height())) // 2)) for image in jumping_throw_right]

jumping_throw_left = [pygame.transform.scale(image, ((int(image.get_width())) // 2, (int(image.get_height())) // 2)) for image in jumping_throw_left]

throw_right = pygame.image.load("Character/Throw__000.png"), pygame.image.load("Character/Throw__001.png"), pygame.image.load("Character/Throw__002.png"), pygame.image.load("Character/Throw__003.png"), pygame.image.load("Character/Throw__004.png"), pygame.image.load("Character/Throw__005.png"), pygame.image.load("Character/Throw__006.png"), pygame.image.load("Character/Throw__007.png"), pygame.image.load("Character/Throw__008.png"), pygame.image.load("Character/Throw__009.png")

throw_left = [pygame.transform.flip(image, 1, 0) for image in throw_right]

throw_right = [pygame.transform.scale(image, ((int(image.get_width())) // 2, (int(image.get_height())) // 2)) for image in throw_right]

throw_left = [pygame.transform.scale(image, ((int(image.get_width())) // 2, (int(image.get_height())) // 2)) for image in throw_left]

kunai_right = pygame.image.load("Character/Kunai.png")

kunai_left = pygame.transform.flip(kunai_right, 1, 0)

kunai_right = pygame.transform.scale(kunai_right, ((int(kunai_right.get_width())) // 2, (int(kunai_right.get_height())) // 2))

kunai_left = pygame.transform.scale(kunai_left, ((int(kunai_left.get_width())) // 2, (int(kunai_left.get_height())) // 2))

idle_right = [pygame.image.load("Character/Idle__000.png"), pygame.image.load("Character/Idle__001.png"), pygame.image.load("Character/Idle__002.png"), pygame.image.load("Character/Idle__003.png"), pygame.image.load("Character/Idle__004.png"), pygame.image.load("Character/Idle__005.png"), pygame.image.load("Character/Idle__006.png"), pygame.image.load("Character/Idle__007.png"), pygame.image.load("Character/Idle__008.png"), pygame.image.load("Character/Idle__009.png")]

idle_left = [pygame.transform.flip(image, 1, 0) for image in idle_right]

idle_right = [pygame.transform.scale(image, ((int(image.get_width())) // 2, (int(image.get_height())) // 2)) for image in idle_right]

idle_left = [pygame.transform.scale(image, ((int(image.get_width())) // 2, (int(image.get_height())) // 2)) for image in idle_left]


class Player():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, 200, 250)
        self.is_jump = False
        self.idle = True
        self.left = False
        self.right = False
        self.throw = False
        self.attack = False
        self.slide = False
        self.walk_count = 0
        self.idle_count = 0
        self.jump_animation_count = 0
        self.throw_count = 0
        self.attack_count = 0
        self.slide_count = 0
        self.vel = 20
        self.jump_count = 10
        self.last = "right"
    def draw(self, win):
        self.hitbox = pygame.Rect(self.x, self.y, 200, 250)
        if not self.is_jump and not self.throw:
            if self.walk_count + 1 >= 40:
                self.walk_count = 0
            if self.idle_count + 1 >= 40:
                self.idle_count = 0
            if self.left:
                self.slide = False
                self.attack = False
                win.blit(walk_left[self.walk_count//4], (self.x, self.y))
                self.walk_count += 1
            elif self.right:
                self.slide = False
                self.attack = False
                win.blit(walk_right[self.walk_count//4], (self.x, self.y))
                self.walk_count += 1
            elif self.attack:
                if self.attack_count + 1 >= 40:
                    self.attack_count = 0
                    self.attack = False
                if self.attack and self.last == "left":
                    win.blit(attack_left[self.attack_count//4], (self.x, self.y))
                    self.attack_count += 1
                elif self.attack and self.last == "right":
                    win.blit(attack_right[self.attack_count//4], (self.x, self.y))
                    self.attack_count += 1
            elif self.slide:
                if self.slide_count + 1 >= 40:
                        self.slide_count = 0
                if self.slide and self.last == "right":
                        win.blit(slide_right[self.slide_count//4], (self.x, self.y + self.height // 4))
                        self.slide_count += 1
                elif self.slide and self.last == "left":
                        win.blit(slide_left[self.slide_count//4], (self.x, self.y + self.height // 4))
                        self.slide_count += 1
            else:
                if self.last == "right":
                    win.blit(idle_right[self.idle_count//4], (self.x, self.y))
                    self.idle_count += 1
                elif self.last == "left":
                    win.blit(idle_left[self.idle_count//4], (self.x, self.y))
                    self.idle_count += 1
        elif not self.throw and self.is_jump:
            if self.jump_animation_count + 1 >= 40:
                self.jump_animation_count = 0
            if self.idle_count + 1 >= 40:
                self.idle_count = 0
            if self.right:
                win.blit(jump_right[self.jump_animation_count//4], (self.x, self.y))
                self.jump_animation_count += 1
            elif self.left:
                win.blit(jump_left[self.jump_animation_count//4], (self.x, self.y))
                self.jump_animation_count += 1
            else:
                if self.last == "right":
                    win.blit(idle_right[self.idle_count//4], (self.x, self.y))
                    self.idle_count += 1
                elif self.last == "left":
                    win.blit(idle_left[self.idle_count//4], (self.x, self.y))
                    self.idle_count += 1
        elif self.throw and self.is_jump:
            if self.throw_count + 1 >= 40:
                self.throw_count = 0
                self.throw = False
            if self.throw and self.last == "left":
                win.blit(jumping_throw_left[self.throw_count//4], (self.x, self.y))
                self.throw_count += 1
            elif self.throw and self.last == "right":
                win.blit(jumping_throw_right[self.throw_count//4], (self.x, self.y))
                self.throw_count += 1
        elif self.throw:
            if self.throw_count + 1 >= 40:
                self.throw_count = 0
                self.throw = False
            if self.throw and self.last == "left":
                win.blit(throw_left[self.throw_count//4], (self.x, self.y))
                self.throw_count += 1
            elif self.throw and self.last == "right":
                win.blit(throw_right[self.throw_count//4], (self.x, self.y))
                self.throw_count += 1




        for kunai_class in kunais:
            if kunai_class.x < 1920 and kunai_class.x > 0:
                if kunai_class.throw:
                    kunai_class.x += kunai_class.vel
            else:
                kunais.pop(kunais.index(kunai_class))

        keys = pygame.key.get_pressed()

class Projectile():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.throw = False
        self.vel = 32 * facing
        self.hit = False
    def draw(self, win):
        if facing == 1:
            win.blit(kunai_right, (self.x, self.y))
        else:
            win.blit(kunai_left, (self.x, self.y))
        


class Block():
    def __init__(self, x, y):
        self.x = x
        self. y = y
        self.hitbox = (self.x, self.y, 100, 100)
    def draw(self, win):
        self.hitbox = (self.x, self.y, 100, 100)
        pygame.draw.rect(win, (0, 0, 25), self.hitbox)

# class Police_Officer():

# class Soldier():

def redraw_game_window(win):
    win.blit(bg, (x, y))
    player.draw(win)
    # player2.draw(win)
    for kunai_class in kunais:
        if player.throw_count == 30:
                kunai_class.throw = True
        if kunai_class.throw:
            kunai_class.draw(win)
    for block_class in blocks:
        block_class.draw(win)


    pygame.display.update()
    pygame.display.flip()

    
facing = 1
kunais = []
blocks = []
standard_vel = 20
block_count = 0
speed_count = 0
speed_multiplier = 1
in_game = True
run = True
clock = pygame.time.Clock()
player = Player(100, 700, idle_right[0].get_width(), idle_right[0].get_height)

while run:
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
    keys = pygame.key.get_pressed()
    if not in_game:
        win.blit(bg, (0, 0))
        write = font.render("Adi is the GOAT", False, (0, 100, 255))
        win.blit(write, (0, 0))
        pygame.display.update()
        pygame.display.flip()
        time.sleep(5)
        blocks.clear()
        standard_vel = 20
        block_count = 0
        speed_count = 0
        speed_multiplier = 1
        in_game = True
    if in_game:
        redraw_game_window(win)
        speed_count += 1
        block_count += 10
        if(speed_count >= 200 * speed_multiplier):
            speed_multiplier += 1
            player.vel += 10
            standard_vel += 10
        for block_class in blocks:
            if player.hitbox.colliderect(block_class.hitbox):
                lose_text = font.render("You Lost!", False, (100, 0, 255))
                win.blit(lose_text, (960, 200))
                pygame.display.update()
                pygame.display.flip()
                in_game = False
                time.sleep(5)
            if block_class.x >= 0:
                block_class.x -= standard_vel
            else:
                blocks.pop(blocks.index(block_class))
        if block_count == 50:
            block_int = randint(1, 10)
            block_count = 0
            if block_int == 10:
                blocks.append(Block(1960, 900))
        if(x <= -3840):
            x = 0
        x -= standard_vel
        player.right = True
        player.last = "right"
        player.left = False
        speed_count += 1
        if not player.is_jump:
            if keys[pygame.K_w]:
                player.is_jump = True
                redraw_game_window(win)
        else:
            if player.jump_count >= -10:
                neg = 1
                if player.jump_count < 0:
                    neg = -1
                player.y -= (player.jump_count ** 2) * 0.5 * neg
                player.jump_count -= 1
                redraw_game_window(win)
            else:
                player.is_jump = False
                player.jump_count = 10
                redraw_game_window(win)
        # if keys[pygame.K_a] and player.x + player.vel > 0:
        #     player.x -= player.vel
        #     player.left = True
        #     player.last = "left"
        #     player.right = False
        #     redraw_game_window(win)
        # elif keys[pygame.K_d] and player.x + player.width + player.vel < 1920:
        #     player.x += player.vel
        #     player.right = True
        #     player.last = "right"
        #     player.left = False
        #     redraw_game_window(win)
        # elif keys[pygame.K_s]:
        #     if player.last == "right":
        #         player.x += player.vel
        #     else:
        #         player.x -= player.vel
        #     player.slide = True
        #     redraw_game_window(win)
        if keys[pygame.K_SPACE]:
            player.throw = True
            redraw_game_window(win)
            if player.throw:
                if player.last == "right":
                    facing = 1
                else:
                    facing = -1
                if len(kunais) <= 5:
                    kunais.append(Projectile(player.x, player.y, kunai_right.get_width(), kunai_right.get_height()))
        elif keys[pygame.K_k]:
            player.attack = True
            redraw_game_window(win)




# Objective of the game: You are a modern-day Robin Hood, robbing big banks and donating the money to charity and to the poor. You have just
# robbed a bank, but this time the police catches you. Now you are in an intese police chase, and have to both run and combat the police with
# your pistol. You can pick up new weapons and powerups to aid you in your escape.
# Endless Runner or Levels?
# Online Sprites or Self-Drawn Characters?