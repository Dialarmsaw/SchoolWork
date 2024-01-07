"""
This program is meant to display the function of the Golgus Apparatus
"""

import turtle
import random
import time

##GLOBAL VARIABLES##
turnRateMin = 10
divide = 2

speed = 1
clockSpeed = 0.1

##SCREEN##
wn = turtle.Screen()
wn.clearscreen()
wn.setup(600, 600)
wn.bgcolor("gray")
#wn.tracer(0)
##GOLGI##
golgi = turtle.Turtle()
golgi.shape("triangle")  #replace with image
golgi.color("black")
golgi.setheading(90)
#set the places it can go, probably 4 total

allProtiens = []


def newProtien():
	protien = turtle.Turtle()
	protien.shape("circle")
	protien.tag = random.randrange(0, 4)  #make tags for destination
	if protien.tag == 0:
    	protien.color("green")
	if protien.tag == 1:
    	protien.color("blue")
	if protien.tag == 2:
    	protien.color("black")
	if protien.tag == 3:
    	protien.color("purple")
	protien.pendown()
	protien.speed(0)
	protien.setheading(random.randrange(0, 360))
	allProtiens.append(protien)
	print(protien.tag)


def moveProtien(protien):
	x = protien.xcor()
	y = protien.ycor()
	heading = protien.heading() + random.randrange(
    	int((turnRateMin + (abs(x) + abs(y)) / divide) * -1),
    	int((turnRateMin + (abs(x) + abs(y)) / divide) + 1))
	protien.setheading(heading)
	protien.fd(speed)


boxes = []


def createBoxes():
	box1 = turtle.Turtle()
	box1.shape("square")
	box1.color("green")
	box1.tag = 0
	box1.penup()
	boxes.append(box1)
	box2 = turtle.Turtle()
	box2.shape("square")
	box2.color("blue")
	box2.tag = 1
	box2.penup()
	boxes.append(box2)
	box3 = turtle.Turtle()
	box3.shape("square")
	box3.color("black")
	box3.tag = 2
	box3.penup()
	boxes.append(box3)
	box4 = turtle.Turtle()
	box4.shape("square")
	box4.color("purple")
	box4.tag = 3
	box4.penup()
	boxes.append(box4)
	boxes[0].goto(0, 100)
	boxes[1].goto(100, 0)
	boxes[2].goto(0, -100)
	boxes[3].goto(-100, 0)


def collision(protien, box):
	if protien.xcor() + 10 > box.xcor() - 15 and protien.xcor(
	) - 10 < box.xcor() + 15:
    	if protien.ycor() + 10 > box.ycor() - 10 and protien.ycor(
    	) - 10 < box.ycor() + 10:
        	return True


createBoxes()
newProtien()

wn.listen()
wn.onkeypress(newProtien, "space")

looptime = 0
while True:
	looptime += 1
	if looptime % 15 == 0:
    	wn.update()
	for protien in allProtiens:
    	print(looptime, " : ", protien.xcor(), ", ", protien.ycor())
    	moveProtien(protien)
    	for box in boxes:
        	if collision(protien, box):
            	if box.tag == protien.tag:
                	allProtiens.remove(protien)
                	newProtien()


