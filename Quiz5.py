import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Change the directory, in order to optimize the code. 
directory = r"F:/Masters/Semester1/APP/Practice/Project/Tkinter/images"
os.chdir(directory)

# Reads the initial images and displays it.
img = cv2.imread("5.jpg", 0)
plt.figure()
f, plot = plt.subplots(2,2)
plot[0][0].imshow(img, cmap="gray")

# Converts the image into an array, and outputs the shape, size of array
array = np.array(img)
print(array.shape)
print(array.size)

# Resizes the array, outputs the shape, size, and dimension
new_arr = np.resize(array,(200,200))
print(new_arr.shape)
print(new_arr.size)
print(new_arr.ndim)

# Writes & Reads the new image
new_img = cv2.imwrite('new_img.jpg', new_arr)
new_img = cv2.imread('new_img.jpg')
plot[0][1].imshow(new_img, cmap='gray')

#using opencv to resize the image
img2 = cv2.resize(img, (800,800))
plot[1][0].imshow(img2, cmap='gray')

#Blurs the image 
img3 = cv2.GaussianBlur(img,(7,7), cv2.BORDER_DEFAULT)
plot[1][1].imshow(img3, cmap="gray")