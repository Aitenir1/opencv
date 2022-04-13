import cv2
import numpy as np

black_img = np.zeros((720, 1280, 3))
random_img = np.random.randint(0, 255, (720, 1280, 3), dtype=np.uint8)
print(random_img)

cv2.imshow('black', black_img)
cv2.imshow('Random', random_img)

cv2.waitKey()