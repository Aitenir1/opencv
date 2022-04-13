import cv2
import numpy as np


def get_contours(image):
    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area > 500:
            peri = cv2.arcLength(cnt, True)
            cv2.drawContours(imgContours, cnt, -1, (255, 0, 0), 1)

            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgContours, (x-5, y-5), (x+w+5, y+h+5), (0, 255, 0), 1)
            if len(approx) == 3:
                figure = 'Triangle'
            elif len(approx) == 4:
                figure = 'Square'
            elif len(approx) > 4:
                figure = 'Circle'
            cv2.putText(imgContours, figure,
                        (x + w // 2 - 10, y + h // 2 - 10),
                        cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 255), 2
                        )
            print(f'Area: {area} \nPerimeter: {peri}\nFigure: {figure}')


img = cv2.imread('media/shapes2.jpeg')
imgContours = np.zeros_like(img)
imgContours.fill(255)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)
imgBlank = np.zeros_like(img)

get_contours(imgCanny)

cv2.imshow('Shapes', img)
cv2.imshow('Gray shapes', imgGray)
cv2.imshow('Blur shapes', imgBlur)
cv2.imshow('Canny shapes', imgCanny)
cv2.imshow('Black', imgBlank)
cv2.imshow('Contours', imgContours)

cv2.waitKey(0)
