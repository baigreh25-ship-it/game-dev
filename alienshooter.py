import pgzrun
import random

WIDTH=600
HEIGHT=500
score=0
alien=Actor("alion.png")
alien.pos=300,250


msg=""

def draw():
    screen.fill("light grey")
    screen.draw.text("ALIEN SHOOTER",(200,50))
    screen.draw.text(msg,(200,80))
    screen.draw.text(f"score:{score}",(100,100))
    alien.draw()

def on_mouse_down(pos):
    global msg,score
    if alien.collidepoint(pos):
        sounds.eep.play()
        alien.x=random.randint(5,550)
        alien.y=random.randint(5,450)
        msg="good shot"
        score+=1
    else:
        msg="you missed haha"
        score-=1



pgzrun.go()