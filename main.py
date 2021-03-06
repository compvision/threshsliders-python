import cv2 as cv
import sys
import Slider as core

core.printVersion()


if (len(sys.argv) != 2):
	print("Usage: python " + str(sys.argv[0]) + " <imgpath>")
	sys.exit()

#cv.namedWindow("Thresholded", cv.WINDOW_NORMAL)
minHue = 0
maxHue = 255
slider = core.Slider(sys.argv[1])

def changeLower(num):
	slider.setMin(minHue)

def changeUpper(num):
	slider.setMax(maxHue)


cv.namedWindow("Threshold Controls", cv.WINDOW_NORMAL)

cv.createTrackbar("hueMin", "Threshold Controls", minHue, 255, changeLower)

cv.createTrackbar("hueMax", "Threshold Controls", maxHue, 255, changeUpper)
while True:
    cv.imshow('image', slider.getImage())
    cv.waitKey(1)
    cv.destroyWindow('image')

'''
img = cv.imread(sys.argv[1])
img = cv.GaussianBlur(img, (3,3), 1, 1)
cvted = cv.cvtColor(img, cv.COLOR_BGR2HSV)
seperated = cv.split(cvted)
hue = seperated[0]
result = img

def thresh():
	a, lower = cv.threshold(hue, minHue, 255, cv.THRESH_BINARY)
	b, upper = cv.threshold(hue, maxHue, 255, cv.THRESH_BINARY_INV)

	result = lower & upper
	return result
	#cv.imshow("Thresholded", result)

def changeLower(num):
	minHue = num
	print("Min Hue: " + str(minHue))

	thresh()

def changeUpper(num):
	maxHue = num	
	print("Max Hue: " + str(maxHue))

	thresh()

cv.namedWindow("Threshold Controls", cv.WINDOW_NORMAL)

cv.createTrackbar("hueMin", "Threshold Controls", minHue, 255, changeLower)

cv.createTrackbar("hueMax", "Threshold Controls", maxHue, 255, changeUpper)
#cv.namedWindow("Thresholded", cv.WINDOW_NORMAL)
#thresh()
while True:
	cv.imshow("Thresholded", result)
	result = thresh()
	cv.waitKey(1)

cv.waitKey(0)
'''