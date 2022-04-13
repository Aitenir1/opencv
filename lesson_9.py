import cv2
import numpy as np

cap = cv2.VideoCapture(0)

cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 150)


colors = {
    'ORANGE': [5, 107, 0, 19, 255, 255],
    # 'YELLOW': [31, 0, 0, 60, 255, 255],
    # 'GREEN': [60, 0, 0, 90, 255, 255]
}


def find_color(image):
    img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    for color, hsv_range in colors.items():
        lower = np.array(hsv_range[:3])
        upper = np.array(hsv_range[3:])

        mask = cv2.inRange(img_hsv, lower, upper)
        cv2.imshow(color, mask)


while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    find_color(img)

    cv2.imshow('video', img)

    cv2.waitKey(1)
