from PIL import Image
import time
import numpy as np
import cv2

# Start here
im2 = cv2.imread("/Users/julia/Desktop/CIS6320/SegmentationAlgorthimImages/BIOUG53847_78_G06.jpg")
# Explore it
print("im2 ndim: ", im2.ndim)
print("im2 shape:", im2.shape)
print("im2 size: ", im2.size)
print("im2 dtype:", im2.dtype)

# cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# cv2.imshow('image', im2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
LUV = cv2.cvtColor(im2, cv2.COLOR_RGB2Luv)
print("luv ndim: ", LUV.ndim)
print("luv shape:", LUV.shape)
print("luv size: ", LUV.size)
print("luv dtype:", LUV.dtype)

# Create an array to store stuff in

# # Define thresholds:
# Lmax = 100
# Umax = 100
# Vmax = 100
#
# # Loop test
# A = time.perf_counter()
# mask = np.random.choice([0], size=(2160, 2880))
# B = time.perf_counter()
# for i in im2:
#     mask[i] = 10
# C = time.perf_counter()
# print(mask.shape, mask.size, mask[:6])
# print(B-A, C-B)

mask = np.random.choice([0], size=(200, 150))

num = LUV[:200, :150, 0]
print(max(np.nditer(num)), min(np.nditer(num)))
for i in range(0, 200):
    for j in range(0, 150):
        if num[i, j] <= 230:
            mask[i, j] = 1
print(im2[:10,:10, 0])
print(LUV[:10,:10, 0])

# cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# cv2.imshow('image', LUV)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#

# Convert BGR to HSV
luv = cv2.cvtColor(im2, cv2.COLOR_RGB2Luv)

# define upper and lower ranges (one value for each channel)
lower = np.array([0, 0, 0])
upper = np.array([150, 150, 150])

# Create the mask
mask = cv2.inRange(luv, lower, upper)

# Bitwise-AND mask and original image
Final = cv2.bitwise_and(im2, im2, mask=mask)

cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.namedWindow('Mask', cv2.WINDOW_NORMAL)
cv2.namedWindow('Final', cv2.WINDOW_NORMAL)
cv2.imshow('Original', im2)
cv2.imshow('Mask', mask)
cv2.imshow('Final', Final)
cv2.waitKey(0)

cv2.bitwise_and()