import numpy as np
import cv2


def empty(a):
    pass
path = 'media/apple.jpeg'

cv2.namedWindow('TrackBars')
cv2.resizeWindow('TrackBars', 640, 240)
cv2.createTrackbar('HUE MIN', 'TrackBars', 0, 179, empty)
cv2.createTrackbar('HUE MAX', 'TrackBars', 179, 179, empty)
cv2.createTrackbar('SAT MIN', 'TrackBars', 0, 255, empty)
cv2.createTrackbar('SAT MAX', 'TrackBars', 255, 255, empty)
cv2.createTrackbar('VALUE MIN', 'TrackBars', 0, 255, empty)
cv2.createTrackbar('VALUE MAX', 'TrackBars', 255, 255, empty)


image = cv2.imread(path)

while True:
    imgHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos('HUE MIN', 'TrackBars')
    h_max = cv2.getTrackbarPos('HUE MAX', 'TrackBars')
    s_min = cv2.getTrackbarPos('SAT MIN', 'TrackBars')
    s_max = cv2.getTrackbarPos('SAT MAX', 'TrackBars')
    v_min = cv2.getTrackbarPos('VALUE MIN', 'TrackBars')
    v_max = cv2.getTrackbarPos('VALUE MAX', 'TrackBars')

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(image, lower, upper)
    imgResult = cv2.bitwise_and(image, image, mask=mask)

    cv2.imshow('Original', image)
    cv2.imshow('HSV', imgHSV)
    cv2.imshow('MASK', mask)
    cv2.imshow('MASK COLOR', imgResult)

    cv2.waitKey(1)