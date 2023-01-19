from datetime import datetime
from dotenv.main import load_dotenv
import os

import cv2
import pandas

static_back = None

motion_list = [None, None]

time = []

load_dotenv()
blur_int = int(os.environ['BLUR'])
print(blur_int)
scores_int = int(os.environ['SCORES'])
print(scores_int)
thresh_int = int(os.environ['THRESH'])
print(thresh_int)
display_setting = os.environ['DISPLAY']
print(display_setting)

df = pandas.DataFrame(columns=["Start", "End"])

video = cv2.VideoCapture(0)
video.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

check, frame = video.read()

while True:

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

    if any(ext == "gray" for ext in display_setting):
        cv2.imshow("Gray Frame", gray2)

    if any(ext == "diff" for ext in display_setting):
        cv2.imshow("Difference Frame", diff_frame)

    if any(ext == "thresh" for ext in display_setting):
        cv2.imshow("Threshold Frame", thresh_frame)

    if any(ext == 'color' for ext in display_setting):
        cv2.imshow("Color Frame", display_frame)

    frame = frame2

    key = cv2.waitKey(1)
    if key == ord('q'):
        if motion == 1:
            time.append(datetime.now())
        break

video.release()

cv2.destroyAllWindows()
