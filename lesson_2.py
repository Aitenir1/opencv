import cv2
import numpy as np

img = cv2.imread('media/photo.jpg')

kernel = np.ones((5, 5), dtype=np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img, (21, 21), 0)
imgCanny1 = cv2.Canny(img, 100, 100)
imgCanny2 = cv2.Canny(img, 200, 200)
imgDilation = cv2.dilate(imgCanny1, kernel=kernel, iterations=1)
imgErosion = cv2.erode(imgDilation, kernel=kernel, iterations=1)


cv2.imshow('GRAY', imgGray)
cv2.imshow('BLUR', imgBlur)
cv2.imshow('CANNY 100', imgCanny1)
cv2.imshow('CANNY 200', imgCanny2)
cv2.imshow('DILATION', imgDilation)
cv2.imshow('EROSION', imgErosion)

cv2.waitKey(0)

