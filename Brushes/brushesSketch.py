
from BrushClass import Brush, HuePoint, ColorPoint, BrightnessPoint, distToColorPoints, distToProbList, weighted_choice
from vectors import calcVector
import time
import sys

#java -Xms6g -Xmx6g -jar procjava -Xms6g -Xmx6g -jar proc

# Set seed values based on system time
rSeed = int(time.time())
nSeed = int(time.time()+25)
randomSeed(rSeed)
noiseSeed(nSeed)
saveImage = True

# Define the global inputs to the system

width  = 2500
height = 1000

# Function to convert from percent of canvas to pixels
def c(percent, side):
	#global width, height
	if (side == 'w'):
		return (percent * width)
	elif (side == 'h'):
		return (percent * height)
	else:
		sys.exit('Chad\'s Comment: \'' + side + '\' passed into pixel to canvas converstion function c')

# Function to return an adjusted randomGaussian()
def positiveGaussian(mean, stdDev):
	adjGuassian = ( randomGaussian() * stdDev ) + mean 
	return int(abs(adjGuassian))


# Set the mean number of brush strokes
meanNumBrushStrokes = 24000
numBrushStrokes   = positiveGaussian(meanNumBrushStrokes, 12000)
meanBrushRadius   = c(0.03, 'h')
meanNumBristles   = 20
meanBristleRadius = positiveGaussian(meanBrushRadius / 16, 5)
packingAttempts   = 10
strokeSteps       = c(0.07, 'h')


def setup():
	global width, height, numBrushStrokes, meanBrushRadius, packingAttempts

	size(width, height)
	colorMode(HSB, 360, 100, 100)
	background(0, 0, 91)

	# This list will store all of the brush objects
	brushes = []
	for i in range(numBrushStrokes):

		# Define an X and Y position for the brush
		x = random(c(0.03,'w'), c(0.97,'w'))
		y = random(c(0.03,'h'), c(0.97,'h'))

		# Set brush radius
		r = positiveGaussian(meanBrushRadius, meanBrushRadius * 0.2)

		# Set the number of attempted bristles
		attemptedNumBristles = positiveGaussian(meanNumBristles, 10)

		# Set the radius for each bristle
		attemptedBristleRadii = []
		for i in range(attemptedNumBristles):
			radius = positiveGaussian(meanBristleRadius, meanBrushRadius*0.1)
			attemptedBristleRadii.append(radius)

		# Create a new Brush object using the parameters that were just defined
		# Brush.__init()__(self, brushX, brushY, brushRadius, numBristles, bristleRadii, bristleColor, packingAttempts)
		brush = Brush(x, y, r, attemptedNumBristles, attemptedBristleRadii, packingAttempts)
		brushes.append(brush)

	# Create the hue points array
	huePoints = []
	huePalette = [85, 73, 310, 333, 25]
	for i in range(len(huePalette)):
		x = random(c(0.1,'w'), c(0.9,'w'))
		y = random(c(0.1,'h'), c(0.9,'h'))
		huePoints.append(HuePoint(PVector(x, y), huePalette[i]))

	# Create the color points array
	colorPoints = []
	colorPalette = [[230,89,21], [0,0,94], [203,56,84], [169,68,73], [0,0,100], [51,66,93]]
	for i in range(len(colorPalette)):
		x = random(c(0.1,'w'), c(0.9,'w'))
		y = random(c(0.1,'h'), c(0.9,'h'))
		colorPoints.append(ColorPoint(PVector(x, y), colorPalette[i][0], colorPalette[i][1], colorPalette[i][2]))

	# Create the brightness points array
	brightnessPoints = []
	bightnessPalette = [44, 44, 15, 30, 66]
	for i in range(len(huePalette)):
		x = random(c(0.1,'w'), c(0.9,'w'))
		y = random(c(0.1,'h'), c(0.9,'h'))
		brightnessPoints.append(BrightnessPoint(PVector(x, y), bightnessPalette[i]))

	# i = 0
	# for b in brushes:
	# 	println('Brush_' + str(i) + ' - Num Bristles: ' + str(b.numBristles) + '\n')
	# 	i += 1

	# for h in huePoints:
	# 	fill(h.color)
	# 	ellipse(h.pX, h.pY, 2, 2)

	# for x in range(width/10):
	# 	for y in range(height/10):
	# 		px = x * 10
	# 		py = y * 10
	# 		nV = calcVector(PVector(px, py), 2)
	# 		nV.mult(1)
	# 		line(px, py, px + nV.x, py + nV.y)
	# 		ellipse(px, py, 2, 2)

	# Draw the brush strokes
	# For each brushStroke
	for bs in brushes:
		# Find distance to color points and select color
		# Want to base color on stroke starting position
		bpV = PVector(bs.brushX, bs.brushY)
		hueDistList = distToColorPoints(bpV, huePoints)
		hueProbList = distToProbList(hueDistList, 2)
		selectedHuePoint = weighted_choice(huePoints, hueProbList)
		brightDistList = distToColorPoints(bpV, brightnessPoints)
		brightProbList = distToProbList(brightDistList, 2)
		selectedBrightPoint = weighted_choice(brightnessPoints, brightProbList)
		colorDistList = distToColorPoints(bpV, colorPoints)
		colorProbList = distToProbList(colorDistList, 2)
		selectedColorPoint = weighted_choice(colorPoints, colorProbList)

		noiseMove = 0
		vectorPicker = random(0,3)
		if (vectorPicker < 1):
			noiseMove = 10000
		elif (vectorPicker < 2):
			noiseMove = 20000
		else:
			noiseMove = 30000

		#noiseMove = 0

		# Step this brushStoke stroke steps
		thisStrokeSteps = positiveGaussian(strokeSteps, strokeSteps * 0.2)
		for s in range(thisStrokeSteps):
			currX = bs.brushX
			currY = bs.brushY
			noiseScale = 0.001
			stepDist = 3

			if ( currX < c(0.03, 'w') or currX > c(0.97, 'w')):
				break
			if ( currY < c(0.06, 'h') or currY > c(0.94, 'h')):
				break
	

			noiseAngle = noise((bs.brushX + noiseMove) * noiseScale , (bs.brushY + noiseMove) * noiseScale) * TWO_PI
			nx = stepDist * sin(noiseAngle)
			ny = stepDist * cos(noiseAngle)

			colorMode(HSB, 360, 100, 100)
			stroke(selectedHuePoint.hue,80,selectedBrightPoint.brightness, 8)
			stroke(selectedColorPoint.hue,selectedColorPoint.saturation,selectedColorPoint.brightness, 4)
			bs.drawBrush(nx, ny)
			#bs.drawBrush(1, 0)
	println('done')

	if (saveImage == True):
		save('output_trial/image_n' + str(nSeed) + '_r' + str(rSeed) + '.tiff')
		output = createWriter('output_trial/image_n' + str(nSeed) + '_r' + str(rSeed) + '.txt')
		output.print('width: ' + str(width) + '\r\n')
		output.print('height: ' + str(height) + '\r\n')
		output.print('meanNumBrushStrokes: ' + str(meanNumBrushStrokes) + '\r\n')
		output.print('numBrushStrokes: ' + str(numBrushStrokes) + '\r\n')
		output.print('meanBrushRadius: ' + str(meanBrushRadius) + '\r\n')
		output.print('meanNumBristles: ' + str(meanNumBristles) + '\r\n')
		output.print('meanBristleRadius: ' + str(meanBristleRadius) + '\r\n')
		output.print('packingAttempts: ' + str(packingAttempts) + '\r\n')
		output.print('attemptedNumBristles: ' + str(attemptedNumBristles) + '\r\n')
		output.print('strokeSteps: ' + str(strokeSteps) + '\r\n')
		output.print('colorPalette: ' + str(colorPalette) + '\r\n')
		output.print('huePalette: ' + str(huePalette) + '\r\n')
		output.print('bightnessPalette: ' + str(bightnessPalette) + '\r\n')
		output.flush()# Writes the remaining data to the file
		output.close()# Finishes the file

	exit()