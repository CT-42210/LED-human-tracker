from datetime import datetime
from dotenv.main import load_dotenv
import os
import numpy as np

import cv2
import pandas

static_back = None

motion_list = [None, None]

time = []

load_dotenv()
display_setting = list(os.environ['DISPLAY_CONFIG'])
blur_int = int(os.environ['BLUR'])
scores_int = int(os.environ['SCORES'])
thresh_int = int(os.environ['THRESH'])
x_res_int = int(os.environ['X_RES'])
y_res_int = int(os.environ['Y_RES'])

df = pandas.DataFrame(columns=["Start", "End"])

video = cv2.VideoCapture(1)
video.set(cv2.CAP_PROP_FRAME_WIDTH, x_res_int)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, y_res_int)

check, frame = video.read()

while video.isOpened():

    check, frame2 = video.read()

    motion = 0

    gray1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    gray1 = cv2.GaussianBlur(gray1, (blur_int, blur_int), 0)
    gray2 = cv2.GaussianBlur(gray2, (blur_int, blur_int), 0)

    if static_back is None:
        static_back = gray1
        continue

    diff_frame = cv2.absdiff(gray1, gray2)

    thresh_frame = cv2.threshold(diff_frame, thresh_int, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    # Copy the thresholded image.
    im_floodfill = thresh_frame.copy()

    # Mask used to flood filling.
    # Notice the size needs to be 2 pixels than the image.
    h, w = thresh_frame.shape[:2]
    mask = np.zeros((h + 2, w + 2), np.uint8)

    # Floodfill from point (0, 0)
    cv2.floodFill(im_floodfill, mask, (0, 0), 255);

    # Invert floodfilled image
    im_floodfill_inv = cv2.bitwise_not(im_floodfill)

    # Combine the two images to get the foreground.
    im_out = thresh_frame | im_floodfill_inv

    display_frame = frame2.copy()

    cnts, _ = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        scores = cv2.contourArea(contour)
        if scores < scores_int:
            continue
        motion = 1

        (x, y, w, h) = cv2.boundingRect(contour)

        cv2.rectangle(display_frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    motion_list.append(motion)

    motion_list = motion_list[-2:]

    if motion_list[-1] == 1 and motion_list[-2] == 0:
        time.append(datetime.now())

    if motion_list[-1] == 0 and motion_list[-2] == 1:
        time.append(datetime.now())

    if any(ext == "g" for ext in display_setting):
        cv2.imshow("Gray Frame", gray2)

    if any(ext == "d" for ext in display_setting):
        cv2.imshow("Difference Frame", diff_frame)

    if any(ext == "t" for ext in display_setting):
        cv2.imshow("Threshold Frame", thresh_frame)

    if any(ext == 'c' for ext in display_setting):
        cv2.imshow("Color Frame", display_frame)

    if any(ext == 'f' for ext in display_setting):
        cv2.imshow("Flood Frame", im_out)

    frame = frame2

    key = cv2.waitKey(1)
    if key == ord('q'):
        if motion == 1:
            time.append(datetime.now())
        break

video.release()

cv2.destroyAllWindows()
