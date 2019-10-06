
def calcVector(pV, vectorName):

	if (vectorName == 1):
		nx = sin(radians(min(pV.x, pV.y)))
		ny = cos(pV.x * pV.y)

	if (vectorName == 2):
		nx = pV.mag()/80
		ny = sin(pV.x)*5

	return PVector(nx, ny)