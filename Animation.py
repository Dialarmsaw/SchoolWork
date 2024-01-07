import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    if GPIO.input(10) == GPIO.HIGH:
        time.sleep(1)
        exec(open('animation.py').read())

################ This code above calls the code below ################

import shapes#imports packages
import random
import time

canvas = shapes.GraphWin("Rocket!",1000, 1000) # creates canvas


star=shapes.Circle(0,50,25) #creates the background star
star.setFill('#E8E830')

bg=shapes.Rectangle(1000,1000,0,0) #creates the background
bg.setFill('#034A4D')

gnd=shapes.Rectangle(0 ,500,1000,1000) #creates the ground
gnd.setFill("#146B0E")

bg.draw(canvas)
star.draw(canvas) #draws star, ground, and background to the screen
gnd.draw(canvas)

xs=50 #starts star x and y
ys=500



fire1=shapes.Polygon(550,550,450,550,500,750) #creates the red fire
fire1.setFill('#E23B3B')

fire2=shapes.Polygon(550,550,450,550,500,750) #creates the orange fire
fire2.setFill('#FF7700')

fire3=shapes.Polygon(550,550,450,550,500,750) #creates the yellow fire
fire3.setFill('#E8E830')

x=500#creates the whole rocket
y=300
body=shapes.Rectangle(x-50,y-50,x+50,y+250)
circ=shapes.Circle(x,y,40)
tri1=shapes.Polygon(x-50,y-50,x+50,y-50,x,y-150)
tri2=shapes.Polygon(x-50,y+150,x-50,y+250,x-100,y+250)
tri3=shapes.Polygon(x+50,y+250,x+50,y+150,x+100,y+250)

circ.setFill('#7A9DC0')
tri1.setFill('#3F5870')
tri2.setFill('#3F5870')
tri3.setFill('#3F5870')
body.setFill('#394958')


body.draw(canvas) #draws the rocket
tri1.draw(canvas)
tri2.draw(canvas)
tri3.draw(canvas)
circ.draw(canvas)

Launch=False
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


rotation=-150 #starts a rotation loop
while True:
    if GPIO.input(10) == GPIO.HIGH:
        Launch=True
    rotation+=1 #adds one to rotation loop each intervole
    star.undraw()
    star=shapes.Circle(xs,ys,25) #remakes the star
    star.setFill('#E8E830')
    if ys<475:
        star.draw(canvas)
   
    xs+=3
    ys=0.03*rotation**2+9 #equation for parabola of the sun
   
    if Launch==True: #moves rocket and fire
        circ.move(0,-7)
        body.move(0,-7)
        tri1.move(0,-7)
        tri2.move(0,-7)
        tri3.move(0,-7)
        fire1.move(0,-7)
        fire2.move(0,-7)
        fire3.move(0,-7)
        if rotation%40==0:
            fire1.undraw()
            fire2.undraw()
            fire3.undraw()
            fire1.draw(canvas)
        if rotation%40==10:
            fire1.undraw()
            fire2.undraw()
            fire3.undraw()
            fire2.draw(canvas)
        if rotation%40==20:
            fire1.undraw()
            fire2.undraw()
            fire3.undraw()
            fire3.draw(canvas)
        if rotation%40==30:
            fire1.undraw()
            fire2.undraw()
            fire3.undraw()
            fire1.draw(canvas)
    time.sleep(0.05) #adds in a delay
