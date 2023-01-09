import cv2

# Create a HOG descriptor
hog = cv2.HOGDescriptor()

# Set the SVM (Support Vector Machine) detector to detect humans
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Open the video capture
cap = cv2.VideoCapture(0)

# Read the first frame
ret, frame = cap.read()

while True:
    # Read the next frame
    ret, next_frame = cap.read()

    # Check if the frames were successfully read
    if not ret:
        break

    # Calculate the absolute difference between the frames
    diff = cv2.absdiff(frame, next_frame)

    # Convert the difference image to grayscale
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    # Threshold the difference image to create a binary mask
    _, mask = cv2.threshold(gray, 25, 255, cv2.THRESH_BINARY)

    # Dilate the mask to fill in holes
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    mask = cv2.dilate(mask, kernel, iterations=2)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Check if any contours have a large enough area to be considered motion
    motion = False
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if w > 50 and h > 50:
            motion = True
            break

    # If motion was detected, check for humans in the next frame
    if motion:
        # Detect humans in the next frame
        humans, _ = hog.detectMultiScale(next_frame)

        # Draw a bounding box around each detected human
        for (x, y, w, h) in humans:
            cv2.rectangle(next_frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Display the resulting frame
    cv2.imshow("Human Detection", next_frame)

    # Set the current frame to the next frame
    frame = next_frame

    # Wait for the user to press a key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture
cap.release()

# Destroy all windows
cv2.destroyAllWindows()
