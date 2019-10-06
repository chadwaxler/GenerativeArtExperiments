from __future__ import division

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


# Needed with Processing 3.0 to define size() using variables or when running outside of PDE
def settings():
    size(width, height)

def setup():
    colorMode(HSB, 360, 100, 100, 1)
    noStroke()

    for i in range(0, width, 1):
        hue = rescale(i, 0, width, 0, 100)
        fill(0, 0, hue)
        rect(0, i, width, 1)

    # save("test.tif")
    # exit()