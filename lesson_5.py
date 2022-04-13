import cv2
import numpy as np

img = cv2.imread('media/kings.jpeg')
pts1 = np.float32([
    [0, 300],
    [467, 300],
    [591, 467],
    [591, 0],
])


cv2.imshow('Kings', img)

print('Hello, world')

cv2.waitKey(0)



