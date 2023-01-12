import cv2

# Initialize the human detector
human_detector = cv2.HOGDescriptor()
human_detector.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Initialize the background subtractor
bg_subtractor = cv2.createBackgroundSubtractorMOG2()

# Open the video
cap = cv2.VideoCapture("video.mp4")

while True:
    # Read the current frame
    _, frame = cap.read()

    # Apply the human detector
    humans, _ = human_detector.detectMultiScale(frame, winStride=(8, 8), padding=(32, 32), scale=1.05)

    # Apply the background subtractor
    fgmask = bg_subtractor.apply(frame)

    # Find contours in the foreground mask
    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize an empty list to hold the bounding boxes
    boxes = []

    # Add the bounding boxes for the humans
    for (x, y, w, h) in humans:
        boxes.append((x, y, x + w, y + h))

    # Add the bounding boxes for the contours
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        boxes.append((x, y, x + w, y + h))

    # Apply non-maximum suppression to remove overlapping boxes
    boxes = cv2.dnn.NMSBoxes(boxes, scores, 0.5, 0.5)

    # Draw the bounding boxes on the frame
    for box in boxes:
        (x, y, w, h) = box
        cv2.rectangle(frame, (x, y), (w, h), (0, 0, 255), 2)

    # Show the frame
    cv2.imshow("Human and Motion Detection", frame)

    # Break the loop if the user presses "q"
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture and close the window
cap.release()
cv2.destroyAll
