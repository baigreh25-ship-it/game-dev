import pgzrun
import random

WIDTH=600
HEIGHT=500

alien=Actor("alion.png")
alien.pos=300,250


msg=""

def draw():
    screen.fill("light grey")
    screen.draw.text("ALIEN SHOOTER",(200,50))
    screen.draw.text(msg,(200,80))
    alien.draw()

def on_mouse_down(pos):
    global msg
    if alien.collidepoint(pos):
        alien.x=random.randint(5,550)
        alien.y=random.randint(5,450)
        msg="good shot"
    else:
        msg="you missed haha"



pgzrun.go()