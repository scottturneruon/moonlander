import random

surface = Actor("surface")
surface.pos = 400, 600
lander = Actor("apollolander")
lander.pos = random.randint(100,700), 100

count=1
HEIGHT = 800
WIDTH = 800
TARGET=Rect((random.randint(100,700),700),(50,50))



def draw():
    screen.clear()
    surface.draw()
    screen.draw.rect(TARGET, (255,0,0))
    lander.draw()
    


def update():
    lander_update()


def lander_update():
    if keyboard.right:
        lander.pos = (lander.x + 5, lander.y)
    if keyboard.left:
        lander.pos = (lander.x - 5, lander.y)
    if keyboard.up:
        lander.pos = (lander.x, lander.y-10)
    landed_lander()
    set_lander_normal()
    

def set_lander_normal():
    global count
    lander.y += (count/7)+1
    count +=1

def landed_lander():
    global count
    if lander.colliderect(TARGET):
        sounds.eep.play()
    elif lander.y>750:
        lander.pos = random.randint(100,700), 100
        count = 1
