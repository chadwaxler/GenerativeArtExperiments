
#########################################################################################################################
#########################                     Start of boiler plate                                   ###################
#########################################################################################################################
#from __future__ import division
# java -Xms6g -Xmx6g -jar procjava -Xms6g -Xmx6g -jar proc

# Start by listing all imports
# from BrushClass import Brush, HuePoint, ColorPoint, BrightnessPoint, distToColorPoints, distToProbList, weighted_choice
# from vectors import calcVector
import time
import sys

# Set seed values based on system time
rSeed = int(time.time())
nSeed = int(time.time()+25)
randomSeed(rSeed)
noiseSeed(nSeed)
saveImage = True

# Define the global inputs to the system
printWidth = 4.0
printHeight = 4.0
dpi = 300

# Derived global variables
width  = int(printWidth * dpi)
height = int(printHeight * dpi)

#########################################################################################################################
#########################                     Sketch specific variables                               ###################
#########################################################################################################################

colors = {'teal': color(170.19, 57.58, 68.65)}


#########################################################################################################################
#########################                     Sketch specific functions                               ###################
#########################################################################################################################

# Function to convert from percent of canvas to pixels
def c(percent, side):
	#global width, height
	if (side == 'w'):
		return (percent * width)
	elif (side == 'h'):
		return (percent * height)
	else:
		sys.exit('Chad\'s Comment: \'' + side + '\' passed into pixel to canvas converstion function c')

# Rescale https://tylerxhobbs.com/essays/2016/working-with-color-in-generative-art
# Used to make gradients
def rescale(value, oldMin, oldMax, newMin, newMax):
    oldSpread = (oldMax - oldMin)
    newSpread = (newMax - newMin)
    newValue  = (newSpread / oldSpread) * (value - oldMin) + newMin
    return newValue


#########################################################################################################################
#########################                     Start of sketch                                         ###################
#########################################################################################################################

# Needed with Processing 3.0 to define size() using variables or when running outside of PDE
def settings():
    size(width, height)

def setup():
    colorMode(HSB, 360, 100, 100, 1)
    background(0,0,100)

    mean1 = random(0, width)
    mean2 = random(0, width)
    for i in range(int(width * 3)):
        xPos = ((width / 60.0) * randomGaussian() + mean1) + ((width / 60.0) * randomGaussian() + mean2)
        fill(222)
        stroke(222)
        point(xPos, height / 2.0)

    # save("test.tif")
    # exit()