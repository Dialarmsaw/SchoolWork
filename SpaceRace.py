import turtle
import random
import time

# global vairables
shipSpeed = 5
asteroidSpeed = 1
startAsteroids = 1
clockSpeed = 0.01

wn = turtle.Screen() #creates a screen
wn.bgcolor("black")
wn.setup(800,800)
wn.tracer(0)


ship1 = turtle.Turtle() # creates a turtle called ship1, this will be the left ship
ship1.penup()
ship1.color("white")
ship1.setheading(90)
ship1.goto(-250, -300)


##### ASTEROID STUFF #####
asteroids = [] # makes a list that will hold all of the asteroids

def makeAsteroids(num):
    for i in range(num): # makes 1 asteroid per num
        asteroid = turtle.Turtle()
        asteroid.penup()
        asteroid.color("white")
        asteroid.shape("circle")
        asteroid.shapesize(0.5)
        asteroid.dir = random.randrange(0,2)
        asteroids.append(asteroid)
    
makeAsteroids(startAsteroids)


def moveAsteroids():
    for asteroid in asteroids:
        x = asteroid.xcor()
        y = asteroid.ycor()
        print(x)
        if x <= -400:
            asteroid.dir = 0
        if x >= 400:
            asteroid.dir = 1
            
        if asteroid.dir == 0:
            asteroid.goto(x + asteroidSpeed, y)
        if asteroid.dir == 1:
            asteroid.goto(x - asteroidSpeed, y)

##### MOVEMENT #####

def leftDown():
    x = ship1.xcor()
    y = ship1.ycor()
    ship1.goto(x, y - shipSpeed)

def leftUp():
    x = ship1.xcor()
    y = ship1.ycor()
    ship1.goto(x, y + shipSpeed)

wn.listen()
wn.onkeypress(leftUp, "w")
wn.onkeypress(leftDown, "s")

while True:
    moveAsteroids()
    
    wn.update()
    time.sleep(clockSpeed)
