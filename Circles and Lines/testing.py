
def setup():
    size(300,300)
    background(150)
    colorMode(HSB, 360, 100, 100, 1)
    
    a = createGraphics(300,300)
    a.beginDraw()
    a.fill(14,255,255)
    a.ellipse(150,150,50,50)
    a.endDraw()
    
    b = createGraphics(300,300)
    b.beginDraw()
    b.fill(255)
    b.ellipse(150,150,25,25)
    b.endDraw()
    
    a.mask(b)
    image(a,0,0)