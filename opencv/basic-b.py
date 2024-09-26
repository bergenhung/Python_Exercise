import cv2 as cv

img = cv.imread('photos/park.jpg')
cv.imshow('Color', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# can only pass odd number, e.g. (3,3) or (7,7)
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(img, 125, 175)
canny2 = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)
cv.imshow('Canny2', canny2)

dilated = cv.dilate(canny, (7,7), iterations = 5)
dilated2 = cv.dilate(canny2, (7,7), iterations = 5)
cv.imshow('Dilated', dilated)
cv.imshow('Dilated2', dilated2)

eroded = cv.erode(dilated, (3,3), iterations = 5)
eroded2 = cv.erode(dilated2, (3,3), iterations = 5)
cv.imshow('Eroded', eroded)
cv.imshow('Eroded2', eroded2)

resized = cv.resize(img, (500, 500), interpolation = cv.INTER_CUBIC)
cv.imshow('Resized', resized)

cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)