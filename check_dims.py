
import cv2
import os

frame_path = r"c:\Users\itsam\OneDrive\Desktop\HTF-Timer\frames\ezgif-frame-001.jpg"
if os.path.exists(frame_path):
    img = cv2.imread(frame_path)
    height, width, layers = img.shape
    print(f"Dimensions: {width}x{height}")
else:
    print("Frame not found")
