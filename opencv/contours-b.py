import cv2 as cv
import numpy as np

img = cv.imread('photos/cats.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
canny = cv.Canny(img, 125, 175)
canny_b = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)
cv.imshow('Canny Blur', canny_b)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

contours_bc, hierarchies_bc = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
contours_t, hierarchies_t = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours_bc)} contours from Canny(Blur) found!')
print(f'{len(contours_t)} contours from Thresh(Gray) found!')

blank_t = np.zeros(img.shape, dtype = 'uint8')
blank_bc = np.zeros(img.shape, dtype = 'uint8')
cv.drawContours(blank_t, contours_t, -1, (0, 0, 255), 1)
cv.drawContours(blank_bc, contours_bc, -1, (0, 0, 255), 1)
cv.imshow('Contours from Threshold', blank_t)
cv.imshow('Contours from Canny', blank_bc)

cv.waitKey(0)