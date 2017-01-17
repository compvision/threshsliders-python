import cv2 as cv
import sys
minHue = 0
maxHue = 255
cv.namedWindow("Thresholded", cv.WINDOW_NORMAL)

if (len(sys.argv) == 3):
	print("Usage: " + str(sys.argv[1]) + " <imgpath>")
	sys.exit()


img = cv.imread(sys.argv[1])
img = cv.GaussianBlur(img, (3,3), 1, 1)
cvted = cv.cvtColor(img, cv.COLOR_BGR2HSV)
seperated = cv.split(cvted)
hue = seperated[0]

def thresh():
	a, lower = cv.threshold(hue, minHue, 255, cv.THRESH_BINARY)
	b, upper = cv.threshold(hue, maxHue, 255, cv.THRESH_BINARY_INV)

	result = lower & upper

	cv.imshow("Thresholded", result)

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

cv.waitKey(0)

