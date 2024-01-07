import turtle
import random
import time

#global var
delay = 0.1
score = 0
a
#screen
wn = turtle.Screen()
wn.clearscreen()
wn.bgcolor("black")
wn.title("Snake (exept this one eats turtles....)")
wn.setup(width=600, height=600)
wn.tracer(0)

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0,0)
head.direction = "stop"

segments = [] #this will hold all of the turtle segments

#food
food = turtle.Turtle()
food.speed(0)
food.shape("turtle")
food.color("red")
food.penup()
food.goto(0,100)

#Functions

def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

def moveSeg():
    #move the segments in reverse order
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    #move segment 0 to head
    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

def reset():
    time.sleep(1)
    head.goto(0,0)
    head.direction = "stop"
    food.goto(0,100)
    
    for segment in segments:
        segment.goto(1000,0)
        
    segments.clear()
    score = 0

#keyboard binding
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_right, "d")

while True:
    wn.update()
    #collision with border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        reset()
    #food stuff
    if head.distance(food) <= 20:
        x = random.randint(-270,270)
        y = random.randint(-270,270)
        food.goto(x,y)
        #add a new segment
        body = turtle.Turtle()
        body.speed(0)
        body.shape("square")
        body.color("green")
        body.penup()
        segments.append(body)
        #shortens the delay
        delay -= 0.001
        #increase the score
        score += 10
        print(score)
    
    #check for collision with body
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            reset()
    
    moveSeg()
    move()
    
    time.sleep(delay)
