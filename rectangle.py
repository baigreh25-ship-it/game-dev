import pgzrun
import random

WIDTH=300
HEIGHT=300


def draw():
    w=WIDTH
    h=HEIGHT-200
    for i in range (20):
        r=255
        g=0
        b=random.randint(100,255)
        rect=Rect((0,0),(w,h))
        rect.center=150,150
        screen.draw.rect(rect,(r,g,b))
        w-=10
        h+=10
        g+=10
        r-=10


pgzrun.go()