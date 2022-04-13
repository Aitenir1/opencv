import cv2

faceCascade = cv2.CascadeClassifier('media/cascade.xml')

image = cv2.imread('media/chulpan.jpg')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(image_gray, 1.1, 4)
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 255), 2)


cv2.imshow('Aitenir', image)

cv2.waitKey(0)
