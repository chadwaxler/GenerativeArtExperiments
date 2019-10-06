

def distToColorPoints(brushPv, colorPoints):
    dist = []
    for p in colorPoints:
        dist.append(PVector.dist(brushPv, p.pV))
    return dist

# Convert Dist to Prob
# https://stackoverflow.com/questions/23459707/how-to-convert-distance-into-probability
def distToProbList(distList, method):
    probList = []
    # (1 / d)
    if (method == 1):
        for d in distList:
            probList.append(1.0/d)
        total = sum(probList)
        probList[:] = [x / total for x in probList]

    # (1 / d^2)
    if (method == 2):
        for d in distList:
            probList.append(1.0/ (d*d))
        total = sum(probList)
        probList[:] = [x / total for x in probList]

    # (1 / d^3)
    if (method == 3):
        for d in distList:
            probList.append(1.0/ (d*d*d))
        total = sum(probList)
        probList[:] = [x / total for x in probList]

    return probList

def weighted_choice(choices, weights):
    total = sum(weights)
    treshold = random(0, total)
    for k, weight in enumerate(weights):
        total -= weight
        if total < treshold:
            return choices[k]

class HuePoint:

    def __init__(self, v, hue):
        self.position = v
        self.pX = v.x
        self.pY = v.y
        self.pV = PVector(v.x, v.y)
        self.hue = hue


class ColorPoint:

    def __init__(self, v, hue, saturation, brightness):
        self.position = v
        self.pX = v.x
        self.pY = v.y
        self.pV = PVector(v.x, v.y)
        self.hue = hue
        self.saturation = saturation
        self.brightness = brightness

class BrightnessPoint:

    def __init__(self, v, brightness):
        self.position = v
        self.pX = v.x
        self.pY = v.y
        self.pV = PVector(v.x, v.y)
        self.brightness = brightness

class Brush:
    """This is a class to define the brush and bristles"""
    
    def __init__(self, brushX, brushY, brushRadius, numBristles, bristleRadii, packingAttempts):
        self.brushX          = brushX
        self.brushY          = brushY
        self.brushRadius     = brushRadius
        self.numBristles     = numBristles
        self.bristleRadii    = bristleRadii
        self.packingAttempts = packingAttempts
        self.bristles        = []
        
        self.packBrush()
        
    def packBrush(self):
        for bristle in range(self.numBristles):
            for attempt in range(self.packingAttempts):
                # Create random X and Y position for bristle
                radius = random(0, self.brushRadius)
                theta  = random(0, TWO_PI)
                x = self.brushX + (radius * cos(theta))
                y = self.brushY + (radius * sin(theta))
                
                # Check if bristle are outside the brush radius
                if ((radius + self.bristleRadii[bristle]) > self.brushRadius):
                    continue
                
                # Check if it is the first bristle, if so then draw it
                if (len(self.bristles) == 0):
                    self.bristles.append(Bristle(x, y, self.bristleRadii[bristle]))
                    break
                    
                # Check if the new bristle overlaps with old bristle
                overlap = False
                for b in self.bristles:
                    d = dist(x, y, b.bristleX, b.bristleY)
                    if ( d < (self.bristleRadii[bristle] + b.bristleRadius) ):
                        overlap = True
                        break
                    
                if (overlap == False):
                    self.bristles.append(Bristle(x, y, self.bristleRadii[bristle]))
                    break

        self.numBristles = len(self.bristles)
            
                
    def drawBrush(self, x, y):
        #ellipse(self.brushX, self.brushY, self.brushRadius, self.brushRadius)
        for bristle in self.bristles:
            strokeWeight(bristle.bristleRadius)
            bristle.drawBristle(x, y)
        self.brushX += x
        self.brushY += y

        
        
class Bristle:
    """This is a class to define a bristle placement, size"""
    
    def __init__(self, bristleX, bristleY, bristleRadius):
        self.bristleX         = bristleX
        self.bristleY         = bristleY
        self.bristleRadius    = bristleRadius
        self.bristleDrawDelay = 0
        
    def drawBristle(self, x, y):
        strokeWeight(self.bristleRadius)
        strokeCap(SQUARE)
        strokeJoin(ROUND)
        smooth()
        line(self.bristleX, self.bristleY, self.bristleX + x, self.bristleY + y)
        self.bristleX += x
        self.bristleY += y

    
    #def setDrawDelay(self):

    #def getDrawDelay(self):

    #def getBristleColor(self):
        
    #def setBristleColor(self):
        
    #def setBristleAlpha(self):
    
    #def setBristleSize(self):
        