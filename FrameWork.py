from PIL import Image
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

# Define thresholds:
Lmax = 100
Umax = 100
Vmax = 100

# Create a loop that scans the array and if it falls within the threshold then assign a 1 to the array

# Or
# identify a mean for back ground and a mean for bug
# Find euclidean distance between each pixel and this mean
# Assign a thershold to see if it is allowed to be in the cluster

# Final array will be a "mask" that can be used to see if the segmentation works

# Metric one, visual
# Working back in RGB colour space can I use this max to up all the R channel to max and B and G to 0 on th eimage
# This would create a red blob showing what I managed to segment out

# Metric two, confusion matrix


