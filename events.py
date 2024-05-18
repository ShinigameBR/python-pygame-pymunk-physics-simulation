import pygame as pg
import sys

def event_management(event):
    if event.type == pg.QUIT:
            pg.quit()
            sys.exit()