import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)


root = tk.Tk()

root.geometry('700x1000')

h_min = tk.Scale(root, from_=0, to=179, orient=tk.HORIZONTAL, label='H MIN')
h_max = tk.Scale(root, from_=0, to=179, orient=tk.HORIZONTAL, label='H max')
s_min = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL, label='S min')
s_max = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL, label='S max')
v_min = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL, label='V min')
v_max = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL, label='V max')

h_min.pack()
h_max.pack()
s_min.pack()
s_max.pack()
v_min.pack()
v_max.pack()


L1 = tk.Label(root, bg='white')
L1.pack()

while True:
    succes, img = cap.read()

    img = cv2.flip(img, 1)

    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #
    # print('NEW PICTURE')
    # print(f'H min: {h_min}')
    # print(f'H max: {h_max}')
    # print(f'S min: {s_min}')
    # print(f'S max: {s_max}')
    # print(f'V min: {v_min}')
    # print(f'V max: {v_max}')
    # print('=============')

    img_hsv = cv2.inRange(
        img,
        np.array([h_min.get(), s_min.get(), v_min.get()]),
        np.array([h_max.get(), s_max.get(), v_max.get()])
    )

    img_hsv = ImageTk.PhotoImage(Image.fromarray(img_hsv))

    L1['image'] = img_hsv

    root.update()