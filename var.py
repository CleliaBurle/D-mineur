import pygame
from pygame.locals import *
import os

# Game Framerate
clock = pygame.time.Clock()
FPS=30

#Resolution
screen_width=800
screen_height=600
screen=pygame.display.set_mode((screen_width, screen_height))

# Colors
black=(0, 0, 0)
red=(255, 0, 0)
blue=(0, 0, 255)

# Font
font = "./utils/balloons.ttf"

# Background Image
bg = pygame.image.load("./utils/image_bg.png")

