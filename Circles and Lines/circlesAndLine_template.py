
#########################################################################################################################
#########################                     Start of boiler plate                                   ###################
#########################################################################################################################
from __future__ import division

# java -Xms6g -Xmx6g -jar procjava -Xms6g -Xmx6g -jar proc
# Start by listing all imports
import time
import sys

# Set seed values based on system time
rSeed = int(time.time())
nSeed = int(time.time()+25)
randomSeed(rSeed)
noiseSeed(nSeed)
saveImage = True

# Define the global inputs to the system
printWidth = 10.0
printHeight = 10.0
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


#########################################################################################################################
#########################                     Sketch specific variables                               ###################
#########################################################################################################################

darkBrown_H = 25.53
darkBrown_S = 19.11
darkBrown_B = 85.47

lightBlack_H = 93
lightBlack_S = 6
lightBlack_B = 15

darkBlue_H = 228.22
darkBlue_S = 75.35
darkBlue_B = 55.69

#########################################################################################################################
#########################                     Sketch specific functions                               ###################
#########################################################################################################################

def pickRandomCoords(width, height, buffer):
    x = random(0 + buffer, width - buffer)
    y = random(0 + buffer, height - buffer)
    return PVector(x, y)

def createGridArray(width, height, gridSize):
    grid = []
    gridCenter = ceil(gridSize/2.0)
    for i in range(int(width/gridSize)):
        for j in range(int(height/gridSize)):
            grid.append({"filled": False, "PVector": PVector((i*gridSize) + gridCenter, (j*gridSize) + gridCenter)})
    return grid

def createdGradientBackground(width, height, direction, stepping, graphic, startColor, endColor):
    if(direction == 'h'):
        numSteps = height / stepping
        for y in range(int(numSteps+1)):
            lerpAmt = rescale(y, 0, numSteps, 0, 1)
            lerpAmt = y * (1.0/numSteps)
            graphic.noStroke()
            graphic.fill(lerpColor(startColor, endColor, lerpAmt))
            xPos = 0
            yPos = y * stepping
            graphic.rect(xPos, yPos, width*2, stepping)
    return


#########################################################################################################################
#########################                     Start of sketch                                         ###################
#########################################################################################################################

# Needed with Processing 3.0 to define size() using variables or when running outside of PDE
def settings():
    size(width, height)

def setup():
    smooth()
    colorMode(HSB, 360, 100, 100, 1)
    background(0, 0, 94)

    grid = createGridArray(width, height, 15)
    filledGridX = []
    filledGridY = []

    source = createGraphics(width, height)
    source.beginDraw()
    source.rectMode(CENTER)
    source.ellipseMode(RADIUS)
    source.colorMode(HSB, 360, 100, 100, 1)
    source.background(20, 4.74, 99.22)
    createdGradientBackground(width, height, 'h', 50, source, color(187,68.05,71), color(187,29,98))
    for i in range(int(random(15, 50))):

        # Select a grid cell at random
        selectedGrid = ceil(random(0, len(grid)-1))

        # If the grid cell is already filled, then continue
        if(grid[selectedGrid]["filled"]):
            continue
        
        # Get the PVector coord
        coords = grid[selectedGrid]["PVector"]

        # If I have already placed an object in either the same column or row of the selected cell, then continue
        if( (coords.x in filledGridX)):
            continue
        if( (coords.y in filledGridY)):
            continue

        # Select color
        randColorPick = random(0, 100)
        if(randColorPick < 15.00):
            currAlpha = random(0.85, 1.0)
            currColor = color(darkBrown_H, darkBrown_S, darkBrown_B, currAlpha) # bark brown
        elif(randColorPick < 25.00):
            currAlpha = random(0.15, 1.0)
            currColor = color(lightBlack_H, lightBlack_S, lightBlack_B, currAlpha) # light black
        else:
            currAlpha = random(0.45, 0.85)
            currColor = color(darkBlue_H, darkBlue_S, darkBlue_B, currAlpha) # dark blue

        source.stroke(currColor)
        source.strokeWeight(int(c(random(0.0003333, 0.0009999), 'w')))
        source.line(coords.x, 0, coords.x, height)
        source.line(0, coords.y, width, coords.y)
        filledGridX.append(coords.x)
        filledGridY.append(coords.y)

        currColor_H = hue(currColor)
        currColor_S = saturation(currColor)
        currColor_B = brightness(currColor)
        currColor_A = alpha(currColor)
        randCircleSize = random(0, 100)
        if(randCircleSize < 10.0):
            radius = c(random(0.025, 0.075), 'w')
        else:
            radius = c(random(0.0025, 0.0115), 'w')
        
        source.noStroke()
        source.fill(20, 4.74, 99.22, 0.8)
        source.ellipse(coords.x, coords.y, radius, radius)

        fuzzy = False

        if(fuzzy):
            for layer in range(3):
                layer_A = currColor_A / 3.0
                layerColor = color(currColor_H, currColor_S, currColor_B, layer_A)
                source.fill(layerColor)
                source.noStroke()
                ossilation = c(random(-0.004, 0.004), 'w')
                randX = random(coords.x - ossilation, coords.x + ossilation)
                randY = random(coords.y - ossilation, coords.y + ossilation)
                source.ellipse(randX, randY, radius, radius)
        else:
            source.fill(currColor)
            source.noStroke()
            source.ellipse(coords.x, coords.y, radius, radius)

    source.endDraw()

    mask = createGraphics(width, height)
    mask.beginDraw()
    mask.rectMode(CENTER)
    mask.ellipseMode(RADIUS)
    mask.background(0)
    mask.fill(255)
    circleArray = []
    for i in range(int(random(1, 50))):
        radius = random(0.01, 0.45) * width
        xRand = random(0, width)
        yRand = random(0, height)
        if(len(circleArray) == 0):
            mask.ellipse(xRand, yRand, radius, radius)
            circleArray.append({'x': xRand, 'y': yRand, 'r': radius})
            continue

        draw = True
        for r in circleArray:
            if(dist(r['x'], r['y'], xRand, yRand) < (r['r'] + radius)):
                draw = False
                break

        if(draw):
            mask.ellipse(xRand, yRand, radius, radius)
            circleArray.append({'x': xRand, 'y': yRand, 'r': radius})
    mask.endDraw()

    source.mask(mask)
    image(source, 0, 0)

    save("rSeed_" + str(rSeed) + ".tif")
    exit()