import cv2

grp_photo = cv2.imread('group-photo.webp')
grayscale = cv2.cvtColor(grp_photo, cv2.COLOR_BGR2GRAY)
# cv2.imwrite('group-photo-gray.webp', grayscale)

c = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces = c.detectMultiScale(grayscale, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
for x, y, w, h in faces:
    if w < 100 and h < 100:
        cv2.rectangle(grp_photo, (x, y), (x+w, y+h), (255, 0, 0))

cv2.imwrite('group-photo-faces.webp', grp_photo)