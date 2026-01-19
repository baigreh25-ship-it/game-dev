import pgzrun
import random

WIDTH=500
HEIGHT=400

score=0
gameover=False
lion=Actor("lion.png")
lion.pos=250,200
antalope=Actor("antalope.png")
antalope.pos=150,120


def draw():
    screen.blit("bgforest.jpg",(0,0))
    lion.draw()
    antalope.draw()
    screen.draw.text("CATCH THE ANTALOPE!!!",(200,50))
    screen.draw.text(f"score:{score}",(40,120))
    if gameover:
        screen.fill("Red")
        screen.draw.text("GAMEOVER",(250,250))
        screen.draw.text(f"Your final score is {score}",(300,200))


def update():
    global score
    if keyboard.up:
        lion.y-=2
    if keyboard.down:
        lion.y+=2
    if keyboard.left:
        lion.x-=2
    if keyboard.right:
        lion.x+=2
    if lion.colliderect(antalope):
        antalope.x=random.randint(50,WIDTH-50)
        antalope.y=random.randint(50,HEIGHT-50)
        sounds.eep.play()
        score+=1

def endgame():
    global gameover
    gameover=True

clock.schedule(endgame,20)


pgzrun.go()