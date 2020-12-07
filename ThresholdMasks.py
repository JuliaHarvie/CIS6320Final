import numpy as np
import cv2

# Please insert what ever path leads to the folder with the input images to run the script
path = "/Users/julia/Desktop/CIS6320/SegmentationAlgorthimImages/"

# Currently have to enter threshold values by hand based off extracting them from imageJ
MeasuredThresholds = np.array([
    [[0, 0, 139], [196, 255, 255]],  # TH1, low, high
    [[0, 0, 127], [204, 255, 255]],  # TH2, low, high
    [[0, 0, 124], [162, 255, 255]],  # TH3, low, high
    [[0, 132, 0], [129, 255, 255]],  # TH4, low, high
    [[0, 0, 135], [195, 255, 255]],  # TH5, low, high
    [[0, 0, 122], [166, 255, 255]],  # TH6, low, high
    [[0, 124, 125], [164, 255, 255]],  # TH7, low, high
    [[0, 0, 115], [18, 255, 255]]])  # TH8, low, high

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


# This function works on one image at a time using values for l, u and v calculated above. It returns the mask
# and an image segmented based off of the mask.
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

# Creating masks and segmentation of all 11 images, using both style of threshold values
TH1Wide = Threshold(cv2.imread(path + "TH1_BIOUG53847_17_B08.jpg"), WideRange)
TH1Average = Threshold(cv2.imread(path + "TH1_BIOUG53847_17_B08.jpg"), AveRange)
TH2Wide = Threshold(cv2.imread(path + "TH2_BIOUG53847_37_D12.jpg"), WideRange)
TH2Average = Threshold(cv2.imread(path + "TH2_BIOUG53847_37_D12.jpg"), AveRange)
TH3Wide = Threshold(cv2.imread(path + "TH3_BIOUG53847_49_E01.jpg"), WideRange)
TH3Average = Threshold(cv2.imread(path + "TH3_BIOUG53847_49_E01.jpg"), AveRange)
TH4Wide = Threshold(cv2.imread(path + "TH4_BIOUG53847_51_E03.jpg"), WideRange)
TH4Average = Threshold(cv2.imread(path + "TH4_BIOUG53847_51_E03.jpg"), AveRange)
TH5Wide = Threshold(cv2.imread(path + "TH5_BIOUG53847_53_E05.jpg"), WideRange)
TH5Average = Threshold(cv2.imread(path + "TH5_BIOUG53847_53_E05.jpg"), AveRange)
TH6Wide = Threshold(cv2.imread(path + "TH6_BIOUG53847_78_G06.jpg"), WideRange)
TH6Average = Threshold(cv2.imread(path + "TH6_BIOUG53847_78_G06.jpg"), AveRange)
TH7Wide = Threshold(cv2.imread(path + "TH7_BIOUG53847_66_F07.jpg"), WideRange)
TH7Average = Threshold(cv2.imread(path + "TH7_BIOUG53847_66_F07.jpg"), AveRange)
TH8Wide = Threshold(cv2.imread(path + "TH8_BIOUG53847_70_F03.jpg"), WideRange)
TH8Average = Threshold(cv2.imread(path + "TH8_BIOUG53847_70_F03.jpg"), AveRange)
UK1Wide = Threshold(cv2.imread(path + "UK1_BIOUG53847_63_F10.jpg"), WideRange)
UK1Average = Threshold(cv2.imread(path + "UK1_BIOUG53847_63_F10.jpg"), AveRange)
UK2Wide = Threshold(cv2.imread(path + "UK2_BIOUG53847_93_H04.jpg"), WideRange)
UK2Average = Threshold(cv2.imread(path + "UK2_BIOUG53847_93_H04.jpg"), AveRange)
GTWide = Threshold(cv2.imread(path + "GT1_BIOUG59392_8_A08.jpg"), WideRange)
GTAverage = Threshold(cv2.imread(path + "GT1_BIOUG59392_8_A08.jpg"), AveRange)

# Write images of both the mask and the final segmented image to a folder
cv2.imwrite("TH1W_mask.jpg", TH1Wide[0])
cv2.imwrite("TH1W_segment.jpg", TH1Wide[1])
cv2.imwrite("TH2W_mask.jpg", TH2Wide[0])
cv2.imwrite("TH2W_segment.jpg", TH2Wide[1])
cv2.imwrite("TH3W_mask.jpg", TH3Wide[0])
cv2.imwrite("TH3W_segment.jpg", TH3Wide[1])
cv2.imwrite("TH4W_mask.jpg", TH4Wide[0])
cv2.imwrite("TH4W_segment.jpg", TH4Wide[1])
cv2.imwrite("TH5W_mask.jpg", TH5Wide[0])
cv2.imwrite("TH5W_segment.jpg", TH5Wide[1])
cv2.imwrite("TH6W_mask.jpg", TH6Wide[0])
cv2.imwrite("TH6W_segment.jpg", TH6Wide[1])
cv2.imwrite("TH7W_mask.jpg", TH7Wide[0])
cv2.imwrite("TH7W_segment.jpg", TH7Wide[1])
cv2.imwrite("TH8W_mask.jpg", TH8Wide[0])
cv2.imwrite("TH8W_segment.jpg", TH8Wide[1])
cv2.imwrite("UK1W_mask.jpg", UK1Wide[0])
cv2.imwrite("UK1W_segment.jpg", UK1Wide[1])
cv2.imwrite("UK2W_mask.jpg", UK2Wide[0])
cv2.imwrite("UK2W_segment.jpg", UK2Wide[1])
cv2.imwrite("GTW_mask.jpg", GTWide[0])
cv2.imwrite("GTW_segment.jpg", GTWide[1])

cv2.imwrite("TH1A_mask.jpg", TH1Average[0])
cv2.imwrite("TH1A_segment.jpg", TH1Average[1])
cv2.imwrite("TH2A_mask.jpg", TH2Average[0])
cv2.imwrite("TH2A_segment.jpg", TH2Average[1])
cv2.imwrite("TH3A_mask.jpg", TH3Average[0])
cv2.imwrite("TH3A_segment.jpg", TH3Average[1])
cv2.imwrite("TH4A_mask.jpg", TH4Average[0])
cv2.imwrite("TH4A_segment.jpg", TH4Average[1])
cv2.imwrite("TH5A_mask.jpg", TH5Average[0])
cv2.imwrite("TH5A_segment.jpg", TH5Average[1])
cv2.imwrite("TH6A_mask.jpg", TH6Average[0])
cv2.imwrite("TH6A_segment.jpg", TH6Average[1])
cv2.imwrite("TH7A_mask.jpg", TH7Average[0])
cv2.imwrite("TH7A_segment.jpg", TH7Average[1])
cv2.imwrite("TH8A_mask.jpg", TH8Average[0])
cv2.imwrite("TH8A_segment.jpg", TH8Average[1])
cv2.imwrite("UK1A_mask.jpg", UK1Average[0])
cv2.imwrite("UK1A_segment.jpg", UK1Average[1])
cv2.imwrite("UK2A_mask.jpg", UK2Average[0])
cv2.imwrite("UK2A_segment.jpg", UK2Average[1])
cv2.imwrite("GTA_mask.jpg", GTAverage[0])
cv2.imwrite("GTA_segment.jpg", GTAverage[1])