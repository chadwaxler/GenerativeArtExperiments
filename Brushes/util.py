
class BrushPlace:
    """This is a class to define the brush and bristles"""
    
    def __init__(self, brushX, brushY, brushRadius, numBristles, bristleRadii, bristleColor, packingAttempts):
        self.brushX          = brushX
        self.brushY          = brushY
        self.brushRadius     = brushRadius
        self.numBristles     = numBristles
        self.bristleRadii    = bristleRadii
        self.bristleColor    = bristleColor
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
                    self.bristles.append(Bristle(x, y, self.bristleRadii[bristle], self.bristleColor[bristle]))
                    break
                    
                # Check if the new bristle overlaps with old bristle
                overlap = False
                for b in self.bristles:
                    d = dist(x, y, b.bristleX, b.bristleY)
                    if ( d < (self.bristleRadii[bristle] + b.bristleRadius) ):
                        overlap = True
                        break
                    
                if (overlap == False):
                    self.bristles.append(Bristle(x, y, self.bristleRadii[bristle], self.bristleColor[bristle]))
                    break
            


                
    def drawBrush(self, x, y):
        noFill()
        stroke(0)
        strokeWeight(2)
        ellipseMode(RADIUS)
        self.brushX += x
        self.brushY += y
        #ellipse(self.brushX, self.brushY, self.brushRadius, self.brushRadius)
        for bristle in self.bristles:
            stroke(bristle.bristleColor)
            strokeWeight(bristle.bristleRadius)
            fill(bristle.bristleColor)
            bristle.drawBristle(x, y)

        
        
class Bristle:
    """This is a class to define a bristle placement, size, and color"""
    
    def __init__(self, bristleX, bristleY, bristleRadius, bristleColor):
        self.bristleX         = bristleX
        self.bristleY         = bristleY
        self.bristleRadius    = bristleRadius
        self.bristleColor     = bristleColor
        self.bristleDrawDelay = 0
        
    def drawBristle(self, x, y):
        line(self.bristleX, self.bristleY, self.bristleX + x, self.bristleY + y)
        self.bristleX += x
        self.bristleY += y

    
    #def setDrawDelay(self):

    #def getDrawDelay(self):

    #def getBristleColor(self):
        
    #def setBristleColor(self):
        
    #def setBristleAlpha(self):
    
    #def setBristleSize(self):
        