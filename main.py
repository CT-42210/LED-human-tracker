import cv2
import numpy as np
import imutils

# Start capturing the video
cap = cv2.VideoCapture(0)

# Create an empty image to store the background
bg = None

# Loop through the first 30 frames
for i in range(30):
    ret, frame = cap.read()
    if bg is None:
        bg = frame.copy().astype("float")
    else:
        cv2.accumulateWeighted(frame, bg, 0.5)

while True:
    ret, frame = cap.read()
    frame_delta = cv2.absdiff(frame, cv2.convertScaleAbs(bg))

    thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]

    kernel = np.ones((3, 3), np.uint8)
    thresh = cv2.dilate(thresh, kernel, iterations=2)
    gray = cv2.cvtColor(thresh, cv2.COLOR_BGR2GRAY)
    cnts = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cnts = imutils.grab_contours(cnts)
    args = {"min_area": 500}

    for c in cnts:
        if cv2.contourArea(c) < args["min_area"]:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("frame", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
