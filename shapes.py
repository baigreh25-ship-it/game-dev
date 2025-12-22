import pgzrun

def draw():
    screen.fill("grey")
    screen.draw.text("shapes",(200,100),color="black")
    screen.draw.filled_circle((200,300),50, color="white")
    screen.draw.rect(Rect((100,100),(50,150)),"red")
    


pgzrun.go()