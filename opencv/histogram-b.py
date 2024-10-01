import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
circle = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)
mask = cv.bitwise_and(gray, gray, mask=circle)
mask_img = cv.bitwise_and(img, img, mask=circle)
cv.imshow('Masked Gray', mask)
cv.imshow('Masked Color', mask_img)

gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    color_hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(color_hist, color=col)
    plt.xlim([0,256])
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.show()


cv.waitKey(0)