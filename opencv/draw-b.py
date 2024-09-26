import cv2 as cv
import numpy as np

blank = np.zeros((500, 600, 3), dtype='uint8')

# 0, 255, 0 - blue, 0, 0, 255 - red, 0, 0, 0 - black, 255, 255, 255 - white
blank[200:300, 200:300] = 255, 255, 255
# cv.imshow('Blank', blank)

cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness = cv.FILLED)
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 25, (255, 0, 0), thickness = cv.FILLED)
cv.line(blank, (blank.shape[1]//2, blank.shape[0]//2), (blank.shape[1], blank.shape[0]), (255, 255, 0), thickness = 3)
cv.putText(blank, 'Hello World', (255, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 255), thickness = 2)
cv.imshow('Craft', blank)

cv.waitKey(0)