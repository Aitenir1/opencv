import queue
import cv2

cap = cv2.VideoCapture(0)

cap.set(3, 2000)
cap.set(4, 1000)
cap.set(10, 100)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    cv2.imshow('video', img)

    if cv2.waitKey(1) and 0xFF == ord('q'):
        break