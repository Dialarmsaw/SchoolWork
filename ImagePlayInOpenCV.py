# Future Features:
    # Add a menu item that takes a current righthand iamge and makes it the main image. That way, you can compose steps.

import numpy as np      #provides arrays needed by cv2
import cv2              #provides tool for importing an image as an array of pixel colors
from tkinter import *   #provides graphics tools (drawing the pictures and GUI (graphical User Interface) tools such as menus and tracking the mouse. 
import copy
from math import floor


window = Tk()
window.title('Image Processing')
window.minsize(height=450, width=875)
window.config(background="white")
aframe = Canvas(window, height = 450, width = 875)  # create a region for drawing two 400x400 pixel images with 2x2 pixels per jpg pixel
aframe.pack()

#input: location of a mouse click (only those in aframe will register) and the image file (global)
#action: determine the colors of the pixel clicked on and print them in the shell
#output: none

def follow(event):
    print("Click location: (" + str(event.x) + ", " + str(event.y)+")")
    height = len(image)
    width = len(image[0])
    xloc = event.x
    yloc = event.y
    if xloc >= 25 and yloc >= 25 and xloc <= 25+2*width and yloc < 25+2*height: # clicked in original picture
        print("BGR:", image[(yloc-25)//2][(xloc - 25)//2])           
    elif xloc >= 450 and yloc >= 25 and xloc <= 450+2*width and yloc < 25+2*height and image2 != []: #clicked in modified image on the right, if it exists
        print("BGR:", image2[(yloc-25)//2][(xloc - 450)//2])          

aframe.bind("<Button-1>", follow)

#input: 0-255 in hex for each color
#action: concatenate into a single string of format "#rrggbb"
#output: the string

def colorswatch(b: int, g: int, r: int):
    colorCode = "#"
    if r>15:
        colorCode += str(hex(r)[-2:])
    else: # for values less than 16, need to include a leading 0.
        colorCode += "0"+str(hex(r)[-1:])
    if g>15:
        colorCode += str(hex(g)[-2:])
    else:
        colorCode += "0"+str(hex(g)[-1:])
    if b>15:
        colorCode += str(hex(b)[-2:])
    else:
        colorCode += "0"+str(hex(b)[-1:])
    return colorCode

#input: image file (of type image) 
#action: combine each pixel trio into one string
#output: reformatted image array

def convertPicture(image):
    tkpic = []
    rowcodes = []
    height = len(image)
    width = len(image[0])
    for row in range(height):
        for column in range(width):
            rowcodes += [colorswatch(image[row][column][0], image[row][column][1], image[row][column][2])]
        tkpic +=[rowcodes]
        rowcodes = []
    return tkpic

#input: image pixel file and new color orders (based on 0, 1, 2)
#action: make each pixel a rearrangement of its colors
#output: new image file

def messWithColor(image, c1, c2, c3):

    height = len(image)
    width = len(image[0])
    global image2
    image2 = []
    imagerow= []
    for c in range(width):
        imagerow += copy.deepcopy([[255,255,255]])
    for r in range(height):  # build an all-white image array
        image2 += [copy.deepcopy(imagerow)]
    for row in range(height):
        for column in range(width): #switch two colors from image to image2
            image2[row][column][0], image2[row][column][1], image2[row][column][2] = image[row][column][c1], image[row][column][c2], image[row][column][c3]
    return image2

#input: image pixel file, location with 0 indicating lefthand image and 1 for rightand image placement
#action: display each pixel as a 2x2 square
#output: none

def displayPicture(tkPic, location):

    height = len(tkPic)
    width = len(tkPic[0])
    for row in range(height):
        for column in range(width):
            aframe.create_rectangle(25+2*column+location*425, 25+2*row, 27+2*column+location*425, 27+2*row, fill = tkPic[row][column], outline = tkPic[row][column])    
        
def tool1(image):
    image2 = messWithColor(image, 2, 0, 1) # Which colors does this call switch (check out the image)? 
    tkPicture2=convertPicture(image2)      # What do other combinations (including repeated values) look like?
    displayPicture(tkPicture2, 1)

#input: image file
#action: There is no Tool2 yet
#output: none

def tool2(image):
    #call another processing def here
    tkPicture2=convertPicture(image)
    displayPicture(tkPicture2, 1)


#input: image
#action: blurr
#output: image
def ChromaKey(image):
    brightnessChange = 75
    height = len(image)
    width = len(image[0])
    global image2
    global image3
    image2 = []
    image3 = []
    imagerow= []
    for c in range(width):
        imagerow += copy.deepcopy([[255,255,255]])
    for r in range(height):  # build an all-white image array
        image2 += [copy.deepcopy(imagerow)]
        image3 += [copy.deepcopy(imagerow)]
    for row in range(height):
        for column in range(width): 
            image2[row][column][0] = image[row][column][0] + brightnessChange
            image2[row][column][1] = image[row][column][1] + brightnessChange
            image2[row][column][2] = image[row][column][2] + brightnessChange
    #return image2
    for row in range(height):
        for column in range(width):
            if image2[row][column][0]+image2[row][column][1]+image2[row][column][2] <750:
                image3[row][column] = image[row][column]
    return image3



def Chrome(image):
    broughted = ChromaKey(image)
    tkPic = convertPicture(broughted)
    displayPicture(tkPic, 1)

'''
def GSAttempt(image):
    offset = 50
    averagecolor = [0,0,0]
    height = len(image)
    width = len(image[0])
    global image2
    image2 = []
    imagerow= []
    for c in range(width):
        imagerow += copy.deepcopy([[255,255,255]])
    for r in range(height):  # build an all-white image array
        image2 += [copy.deepcopy(imagerow)]
    for row in range(height):
        for column in range(width): 
            averagecolor[0] += image[row][column][0]
            averagecolor[1] += image[row][column][1]
            averagecolor[2] += image[row][column][2]
    averagecolor[0] = averagecolor[0]/width*height
    averagecolor[0] = averagecolor[0]/width*height
    averagecolor[0] = averagecolor[0]/width*height
    for row in range(height):
        for column in range(width): 
            if image[row][column][0] > averagecolor[0]+offset or image[row][column][0] < offset*-1 and image[row][column][1] > averagecolor[0]+offset or image[row][column][1] < offset*-1 and image[row][column][2] > averagecolor[2]+offset or image[row][column][2] < offset*-1:
'''


#input: image
#action: crop image
#output: image
def blurr(image, size):
    height = len(image)
    width = len(image[0])
    global image2
    image2 = []
    imagerow= []
    for c in range(width):
        imagerow += copy.deepcopy([[255,255,255]])
    for r in range(height):  # build an all-white image array
        image2 += [copy.deepcopy(imagerow)]
    for row in range (floor(height/2)):
        for column in range(floor(width/2)): 
            averageR = (image[row][column][0] + image[row-1][column][0] + image[row][column-1][0] + image[row-1][column-1][0]) / 4 #get average RGB values for all 4 spaces
            averageG = (image[row][column][1] + image[row-1][column][1] + image[row][column-1][1] + image[row-1][column-1][1]) / 4
            averageB = (image[row][column][2] + image[row-1][column][2] + image[row][column-1][2] + image[row-1][column-1][2]) / 4            
            image2[row][column][0] = averageR        #set the pixels to the average R, G, and B
            image2[row-1][column][0] = averageR
            image2[row][column-1][0] = averageR
            image2[row-1][column-1][0] = averageR

            image2[row][column][1] = averageG
            image2[row-1][column][1] = averageG
            image2[row][column-1][1] = averageG
            image2[row-1][column-1][1] = averageG

            image2[row][column][2] = averageB
            image2[row-1][column][2] = averageB
            image2[row][column-1][2] = averageB
            image2[row-1][column-1][2] = averageB
    return image2 #return finished image

def dispBlurr(image):
    cropped = blurr(image, 2)
    tkPic = convertPicture(cropped)
    displayPicture(tkPic, 1)
#input: image file name
#action: set up menus; import image file data; create a graphics window; call picture painter
#output: none

def whateverthiswas():
    pass

def sccale(image, scale):  # Shrink while throwing away 
    height = len(image)
    width = len(image[0])
    global image2
    image2 = []
    imagerow= []
    for c in range(width):
        imagerow += copy.deepcopy([[255,255,255]])
    for r in range(height):  # build an all-white image array
        image2 += [copy.deepcopy(imagerow)]
    for row in range (floor(height/scale)):
        for column in range(floor(width/scale)): 
            image2[row][column] = image[row*scale][column*scale]
    return image2

def dispCrop(image):
    scale = int(input("What is the scale? (Bigger input makes smaller image) >>> "))
    cropped = scale(image, scale)
    tkPic = convertPicture(cropped)
    displayPicture(tkPic, 1)


def betterScale(image, factor):
    height = len(image)
    width = len(image[0])
    global image2
    image2 = []
    imagerow= []
    for c in range(width):
        imagerow += copy.deepcopy([[255,255,255]])
    for r in range(height):  # build an all-white image array
        image2 += [copy.deepcopy(imagerow)]
    averageR = 0
    averageG = 0
    averageB = 0
    for row in range (floor(height/factor)): #for every scaled pixel
        for column in range(floor(width/factor)): 
            for i in range(factor): #for the scaling
                for n in range(factor):
                    averageR += image[row*factor+i][column*factor+n][0] #get the average rgb's for the square around the pixel
                    averageG += image[row*factor+i][column*factor+n][1]
                    averageB += image[row*factor+i][column*factor+n][2]
            image2[row][column][0] = floor(averageR/factor**2) #set image2 pixel to that average rgb
            image2[row][column][1] = floor(averageG/factor**2)
            image2[row][column][2] = floor(averageB/factor**2)
            averageR = 0 #reset r, g, and b
            averageG = 0
            averageB = 0
    return image2

def dispScaleBetter(image):
    scale = 2
    scaled = betterScale(image, scale)
    tkPic = convertPicture(scaled)
    displayPicture(tkPic, 1)
    cropped = sccale(image, scale)
    tkPic = convertPicture(cropped)
    displayPicture(tkPic, 0)


def darken(image, scale):
    image2 = copy.deepcopy(image)
    height = len(image2)
    width = len(image2[1])
    for row in range(height):
        for column in range(width):
            image2[row][column][0] /= scale
            image2[row][column][1] /= scale
            image2[row][column][2] /= scale
    return image2

def darkentool(image):
    scales = 3
    scale = scales[0] 
    darked = darken(image, scale)
    tkPic = convertPicture(darked)
    displayPicture(tkPic, 1)

def difference(num1, num2):
    difference = num2 - num1
    return abs(difference)

def findEdges(image):
    height = len(image)
    width = len(image[0])
    global image2
    image2 = []
    imagerow= []
    biggestDif = 40
    for c in range(width):
        imagerow += copy.deepcopy([[255,255,255]])
    for r in range(height):  # build an all-white image array
        image2 += [copy.deepcopy(imagerow)]
    for row in range(height):
        for column in range(width): #switch two colors from image to image2
            red1 = image[row][column][0]
            green1 = image[row][column][1]
            blue1 = image[row][column][2]
            try:
                red2 = image[row+1][column][0]
                green2 = image[row+1][column][1]
                blue2 = image[row+1][column][2]
            except IndexError:
                red2 = image[row-1][column][0]
                green2 = image[row-1][column][1]
                blue2 = image[row-1][column][2]

            if difference(red1, red2) > biggestDif and difference(green1, green2) > biggestDif and difference(blue1, blue2) > biggestDif:
                image2[row][column] = [255, 255, 255]
            else:
                image2[row][column] = [0, 0, 0]
        
    return image2

def dispEdges(image):
    edgeImage = findEdges(image)
    tkPic = convertPicture(edgeImage)
    displayPicture(tkPic, 1)

def setup(filename):
 #set up menus
    menubar = Menu(window)
    window.config(menu=menubar)
    ToolsMenu = Menu(menubar)
    ToolsMenu.add_command(label="Mess With Colors", command= lambda: tool1(image)) #put desired parameters in call to Tool1. You can rename Tool1 and 2 to indicate their actual function
    ToolsMenu.add_command(label="Original", command= lambda: tool2(image)) #put desired parameters in call to Tool2
    ToolsMenu.add_command(label = "Chroma Key", command= lambda: Chrome(image))
    ToolsMenu.add_command(label = "Scaled", command= lambda: dispCrop(image))
    ToolsMenu.add_command(label = "Scaled but Better", command= lambda: dispScaleBetter(image))
    ToolsMenu.add_command(label= "Chroma Key", command= lambda: Chrome(image))
    ToolsMenu.add_command(label= "Edges", command= lambda: dispEdges(image))
    #add extra menus here
    menubar.add_cascade(label="Tools", menu=ToolsMenu)

    global image, image2
    image2 = []
    image = cv2.imread(filename)  #read in RGB levels for each pixel. preferred size 200x200 pixel jpgs
    tkPicture = convertPicture(image)  # convert colors represented as three 0-255 blue, green, red levels to one string readable by tkinter (the format is the pound symbol followed by three two-digit hexadecimal numbers 00-ff is same as 0-255 (e.g, #ffff00 is yellow)
    displayPicture(tkPicture, 0)
    window.mainloop()

setup("./JoshuaAbrams-pixelated.jpg")  
#setup("LauraNonsquare.jpg")
#setup("ErnieCircle.jpg")
