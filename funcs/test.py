import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.geometry('500x500')
image1 = Image.open("../media/apple.jpeg")
test = ImageTk.PhotoImage(image1)

label1 = tk.Label(image=test)
label1.image = test

label1.place(x=5, y=5)


root.mainloop()