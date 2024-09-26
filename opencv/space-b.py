import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('photos/park.jpg')
cv.imshow('Park', img)

plt.imshow(img)
plt.show()

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV', hsv)
cv.imshow('HSV2BGR', hsv_bgr)

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
lab_bgr = cv.cvtColor(lab, cv.COLOR_Lab2BGR)
cv.imshow('LAB', lab)
cv.imshow('LAB2BGR', lab_bgr)

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)
plt.imshow(rgb)
plt.show()

cv.waitKey(0)