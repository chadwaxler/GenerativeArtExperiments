
def drawRect(Ox, Oy, width, height, numPoints):
    pointSpacing = float(width) /numPoints
    rectPoints = []
    rectTopPoints = []
    rectRightPoints = []
    rectBottomPoints = []
    rectLeftPoints = []

    ellipseMode(RADIUS)
    stroke(0)
    noFill()
    # Iterate over the top/bottom of rectangle
    y_top = Oy
    y_bottom = Oy + height
    for nWidth in range(numPoints):
        rectTopPoints.append([Ox + (nWidth * pointSpacing), y_top])
        rectBottomPoints.append([Ox + (nWidth * pointSpacing), y_bottom])

    # Iterate over the sides of the rectangle
    x_left = Ox
    x_right = Ox + width
    for nHeight in range(numPoints - 2):
        rectRightPoints.append([x_right, Oy + ((nHeight + 1) * pointSpacing)])
        rectLeftPoints.append([x_left, Oy + ((nHeight + 1) * pointSpacing)])

    print(rectTopPoints)
    print(rectBottomPoints)
    print(rectRightPoints)
    print(rectLeftPoints)


def drawGrid(spacing, width, height):
    w_n = width / spacing
    h_n = height / spacing

    for x in range(w_n):
        x_p = 0 + (x+1) * w_n
        stroke(0)
        line(x_p, 0, x_p, height)
    
    for y in range(h_n):
        y_p = 0 + (y+1) * h_n
        stroke(0)
        line(0, y_p, width, y_p)
    

def setup():
    width = 500
    height = 500

    # Create the canvas
    size(500, 500)

    drawGrid(10, width, height)
    drawRect(50, 50, 250, 250, 5)