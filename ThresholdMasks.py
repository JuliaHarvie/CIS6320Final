from PIL import Image
import time
import numpy as np
import glob
import cv2

# Read in the file path for every image
files = glob.glob("/Users/julia/Desktop/CIS6320/SegmentationAlgorthimImages/*")
# Now I need to store them in a place that will also allow me to attach threshold values
AllImage = {
    "image1": files[0]
}
print(AllImage["image1"])

# #This function works on one image at a time using values for l, u and v calculated about
# def Threshold(InputImg, l, u, v):
#     # Convert Input Image from RGB to luv
#     LUV = cv2.cvtColor(InputImg, cv2.COLOR_RGB2Luv)
#     # Check the bite type. Expecting 8 bite for all but just in case
#     if LUV.dtype == "uint8":
# # If this is true then open cv has scaled the pixels from luv colour shape range to 0:255
#
#
#
# # This version involves a single import of every image
# img = cv2.imread("/Users/julia/Desktop/CIS6320/SegmentationAlgorthimImages/BIOUG53847_78_G06.jpg")
# luvThreshold(img)
