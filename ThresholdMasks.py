from PIL import Image
import time
import numpy as np
import glob
import cv2

# Read in the file path for every image
files = glob.glob("/Users/julia/Desktop/CIS6320/SegmentationAlgorthimImages/*")
# Currently have to enter threshold values by hand based off extracting them from imageJ
# Note these are in lab not luv
MeasuredThresholds = np.array([
    [[0, 0, 139], [196, 255, 255]],  # TH1, low, high
    [[0, 0, 127], [204, 255, 255]],  # TH2, low, high
    [[0, 0, 124], [162, 255, 255]]])  # TH3, low, high
given = MeasuredThresholds.shape[2]
# Calculate low limit and upper limit for each channel by averaging the manually extracted values
AveRange = np.array([[np.mean(MeasuredThresholds[:given, 0, 0]),  # low, l u v
                      np.mean(MeasuredThresholds[:given, 0, 1]),
                      np.mean(MeasuredThresholds[:given, 0, 2])],
                     [np.mean(MeasuredThresholds[:given, 1, 0]),  # high, l u v
                      np.mean(MeasuredThresholds[:given, 1, 1]),
                      np.mean(MeasuredThresholds[:given, 1, 2])]], dtype="int")
# Calculate low limit and upper limit for each channel by choice the values that encompass every extracted value
WideRange = np.array([[min(MeasuredThresholds[:given, 0, 0]),  # low, l u v
                       min(MeasuredThresholds[:given, 0, 1]),
                       min(MeasuredThresholds[:given, 0, 2])],
                      [max(MeasuredThresholds[:given, 1, 0]),  # high, l u v
                       max(MeasuredThresholds[:given, 1, 1]),
                       max(MeasuredThresholds[:given, 1, 2])]], dtype="int")


# This function works on one image at a time using values for l, u and v calculated about
def Threshold(InputImg, Range):
    # Check the bite type. Expecting 8 bite for all but just in case
    if InputImg.dtype != "uint8":
        print("not 8 bite: " + InputImg.dtype)
    # Convert Input Image from RGB to luv
    Luv = cv2.cvtColor(InputImg, cv2.COLOR_RGB2Luv)
    # Define the mask
    mask = cv2.inRange(Luv, Range[0], Range[1])
    # Apply mask to original image
    segmented = cv2.bitwise_and(InputImg, InputImg, mask=mask)
    return mask, segmented


def Display(Original, Threshold):
    cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
    cv2.namedWindow('Mask', cv2.WINDOW_NORMAL)
    cv2.namedWindow('Segmented', cv2.WINDOW_NORMAL)
    cv2.imshow('Original', Original)
    cv2.imshow('Mask', Threshold[0])
    cv2.imshow('Segmented', Threshold[1])
    cv2.waitKey(0)


One = Threshold(cv2.imread(files[0]), WideRange)
Display(cv2.imread(files[0]), One)
