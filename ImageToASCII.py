import cv2 #this imports openCV, which is only used for reading the image
import copy #this imports copy, which is only used for duplicating a list
from math import floor #again, only used once, to floor a number
import sys #this is used to halt the program if there is an error


#global variables
global image
global asciiChars

isCustom = input("Do you want to make your own list of ASCII characters? (y/n) >>> ") #asks the user if they want to make a custom character list

def getChars(isCustom):
    #input: yes or no
    #action: set the list to a custom list or the default
    asciiChars = []
    if isCustom == "y":
        print("REMEMBER! The order you give them is important! It should be from lightest to darkest!")
        howMany = int(input("How many characters do you want? >>> ")) #gets the amount of characters
        for i in range(howMany):
            char = input("What is your character? >>> ") #gets all the character and append them to the character list
            asciiChars.append(char)
        print("This is your list:", asciiChars)
        return asciiChars
    elif isCustom == "n":
        asciiChars = ["@", "#" ,"S" ,"%" ,"?" ,"*" ,"+" , ";", ":", ",", ".",] #default list
        return asciiChars
    else:
        print("You gave a crummy answer. Im going to assume you meant no.")


filename = input("Give me the image file location >>> ") #gets the location of the image file
for char in filename: #replace all bad characters with good characters
    if char == '\\':
        char = "/"
    if char == '"':
        char =''

newFile = input("Give me a name you want the file to be called >>> ") #gets a file name
File = newFile + ".txt" #adds '.txt' to the end of the file name, making it a text file
print("This may take a while. I will inform you when it is done!")

image = cv2.imread(filename) #read the image file
asciiChars = getChars(isCustom) #defines the character list


def getBrightness(r: int, g: int, b: int):
    #input: r, g, g
    #action: get the grayscale value
    #output: the grayscale value
    gray = (int(r)+int(g)+int(b))/3
    return gray

def getASCII(value):
    #input: grayscale value
    #action: find the ascii char that corresponds to that
    #return ascii char
    colorRange = 255
    asciiRange = len(asciiChars)
    asciiValue = floor((value*asciiRange) / colorRange)
    asciiChar = asciiChars[asciiValue-1] #float division
    return asciiChar

def imageToASCIIList(image):
    #input: image
    #action: turn the image into ascii text
    #output: ascii text
    try:
        height = len(image)
        width = len(image[0])
        asciiImage = []
        imagerow = []
        for c in range(width): #for the length of list
            imagerow += copy.deepcopy([[]])
        for r in range(height):  # build an all-white image array
            asciiImage += [copy.deepcopy(imagerow)]
        for row in range(height):
            for column in range(width):
                gray = getBrightness(image[row][column][0], image[row][column][1], image[row][column][2]) #get the brightness of all pixels
                asciiChar = getASCII(gray) #get the ascii char the correlates to the gray
                asciiImage[row][column] = asciiChar #set the corresponding place to the character
        return asciiImage
    except TypeError:
        print("There was an error with the image. Please try again.")
        sys.exit(0)

asciiImage = imageToASCIIList(image) #get the ascii list
height = len(asciiImage) #gets the height and length of the ascii list
width = len(asciiImage[0])
print("The width is:", width, "The Height is:", height) #print the width and length of the image

file = open(File,"a") #open or create a text file

for row in range(height):
    for column in range(width):
        file.write(asciiImage[row][column]) #for every item in the list, type it to the file that was opened
    file.write("\n") #write a new line

file.close()
print("The file has been made! Go check for it in the same directory as this script!")
