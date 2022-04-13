import cv2
from cv2 import VideoCapture

cap = cv2.VideoCapture('media/video.MP4')


while True:
    success, img, = cap.read()

    if success:
        cv2.imshow('video1', img)
    else:
        print('Programm ends')
        break

    cv2.waitKey(1000)