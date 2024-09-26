import cv2 as cv

img = cv.imread('photos/cats.jpg')
cv.imshow('Cats', img)

avg = cv.blur(img, (7, 7))
cv.imshow('Average', avg)

gauss = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow('Gauss', gauss)

medium = cv.medianBlur(img, 5)
cv.imshow('Medium', medium)

bilateral = cv.bilateralFilter(img, 10, 35, 35)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)