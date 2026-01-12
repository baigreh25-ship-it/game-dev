import pgzrun
import random

WIDTH=500
HEIGHT=400

score=0
lion=Actor("lion.png")
lion.pos=250,200
antalope=Actor("antalope.png")
antalope.pos=150,120


def draw():
    screen.fill("light grey")
    lion.draw()
    antalope.draw()
    screen.draw.text("CATCH THE ANTALOPE!!!",(200,50))
    screen.draw.text(f"score:{score}",(40,120))

def update():
    if keyboard.up:
        lion.y-=2
    if keyboard.down:
        lion.y+=2
    if keyboard.left:
        lion.x-=2
    if keyboard.right:
        lion.x+=2
    
pgzrun.go()