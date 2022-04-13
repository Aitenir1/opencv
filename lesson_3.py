import cv2

img = cv2.imread('media/lambo.jpeg')
width = img.shape[0]
height = img.shape[1]

imgResized = cv2.resize(img, (300, 200))
imgCropped = img[int(width * 0.3):int(width * 0.7), int(height * 0.3):int(height * 0.7)]

cv2.imshow('Original', img)
cv2.imshow('Resized', imgResized)
cv2.imshow('Cropped', imgCropped)

cv2.waitKey(0)