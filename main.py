import cv2

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

    # Extract bounding boxes from the contours
    boxes = [cv2.boundingRect(contour) for contour in contours]

    # Apply non-maximum suppression to merge overlapping boxes
    confidence_scores = [1.0] * len(boxes)
    confidence_threshold = 0.5
    overlap_threshold = 0.5
    boxes = cv2.dnn.NMSBoxes(boxes, confidence_scores, confidence_threshold, overlap_threshold)

    # Draw the bounding box on the frame
    for box in boxes:
        x, y, w, h = box
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Display the resulting frame
        cv2.imshow("Motion Detection", frame)

        # Wait for the user to press a key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Release the video capture
    cap.release()

    # Destroy all windows
    cv2.destroyAllWindows()
