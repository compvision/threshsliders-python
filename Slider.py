import cv2 as cv

class Slider(object):
	"""docstring for Slider"""
	def __init__(self, src):
		super(Slider, self).__init__()
		image = cv.imread(src)
		image = cv.GaussianBlur(image, (3,3), 1, 1)
		cvted = cv.cvtColor(image, cv.COLOR_BGR2HSV)
		seperated = cv.split(cvted)
		hue = seperated[0]
		self.img = hue
		self.min = 0
		self.max = 255

	def getImage(self):
		return self.img

	def setMin(self, val):
		self.min = val
		self.thresh()

	def setMax(self, val):
		self.max = val
		self.thresh()

	"""private methods"""

	def thresh(self):
		a, lower = cv.threshold(self.img, self.min, 255, cv.THRESH_BINARY)
		b, upper = cv.threshold(self.img, self.max, 255, cv.THRESH_BINARY_INV)

		self.img = lower & upper
		#return result

def printVersion():
	print("Version 1.0")