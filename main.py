import pygame as pg
import pymunk as pm

from events import event_management
from funcs import create_ball, create_static_ball, draw_balls, draw_static_balls

pg.init()
window = pg.display.set_mode((600, 600))
pg.display.set_caption("Physics Test")

clock = pg.time.Clock()
space = pm.Space()
space.gravity = (0, 100)
balls = []
balls.append(create_ball(space))
static_balls = []
static_balls.append(create_static_ball(space))

while True:
    for event in pg.event.get():
        event_management(event)
    
    window.fill((127, 127, 127))
    draw_balls(window, balls)
    draw_static_balls(window, static_balls)
    space.step(1/50)
    pg.display.update()
    clock.tick(120)