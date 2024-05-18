import pygame as pg
import pymunk as pm

def create_ball(space):
    body = pm.Body(1, 100, body_type = pm.Body.DYNAMIC)
    body.position = (300, 0)
    shape = pm.Circle(body, 60)
    space.add(body, shape)
    return shape

def draw_balls(window, balls):
    for ball in balls:
        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)
        pg.draw.circle(window, (0, 0, 0), (pos_x, pos_y), 60)
        
def create_static_ball(space):
    body = pm.Body(body_type=pm.Body.STATIC)
    body.position = (350, 400)
    shape = pm.Circle(body, 40)
    space.add(body, shape)
    return shape

def draw_static_balls(window, balls):
    for ball in balls:
        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)
        pg.draw.circle(window, (0, 0, 0), (pos_x, pos_y), 40)

