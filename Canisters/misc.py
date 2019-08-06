import pygame

import random
from pygame.locals import *
from enum import Enum
####################################################################

#initialization stuffs DO NOT TOUCH
pygame.init()
# popup window stuff /D
win_len = 1200
win_ht = 600
WIN = pygame.display.set_mode((win_len, win_ht),pygame.FULLSCREEN)




pygame.display.set_caption('CANISTERS')
font = pygame.font.SysFont("comicsansms", 20)
text = font.render("Score=", False, (0, 0, 0))



WIN.blit(text, (0, 0))
# hides the mouse from view /
pygame.mouse.set_visible(True)
# color values /D
red = (200, 0, 100)
green = (100, 200, 100)
aqua = (100, 200, 200)
blue = (140,120,210)
yellow = (250, 230, 0)
teal = (0, 255, 255)
black = (0, 0, 0)
white = (255, 255, 255)
#######################################################################
random.seed()


# calculate depth of collision
# def GetIntersectionDepth(rect_A, rect_B):
#     # Calculate half sizes.
#     halfWidthA = rect_A.width / 2
#     halfHeightA = rect_A.height / 2
#     halfWidthB = rect_B.width / 2
#     halfHeightB = rect_B.height / 2
#
#     # calculate centers
#     center_A = Vector(rect_A.left + halfWidthA, rect_A.top + halfHeightA)
#     center_B = Vector(rect_A.left + halfWidthA, rect_A.top + halfHeightA)
#
#     # Calculate current and minimum-non-intersecting distances between centers.
#     distance_x = center_A.x - center_B.x
#     distance_y = center_A.y - center_B.y
#     minDistance_x = halfWidthA + halfWidthB
#     minDistance_y = halfHeightA + halfHeightB
#
#     # If we are not intersecting at all, return (0, 0).
#     if distance_x >= minDistance_x and distance_y >= minDistance_y:
#         return Vector.Zero
#
#     # Calculate and return intersection depths
#     if distance_x > 0:
#         depth_x = minDistance_x - distance_x
#     else:
#         depth_x = -minDistance_x - distance_x
#
#     if distance_x > 0:
#         depth_y = minDistance_y - distance_y
#     else:
#         depth_y = -minDistance_y - distance_y
#
#     return Vector(depth_x, depth_y)