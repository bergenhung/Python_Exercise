import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    # images, videos, and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # only for live videos -> not tried in any code
    capture.set(3,width)
    capture.set(4,height)

img = cv.imread('photos/cat_large.jpg')
cv.imshow('Cat Large', img)
cv.imshow('Cat Resized', rescaleFrame(img, 0.25))

cv.waitKey(0)

capture = cv.VideoCapture('videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, 0.5)
    
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()