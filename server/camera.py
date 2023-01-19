import cv2

# Initialize the camera
cap = cv2.VideoCapture(0)

while True:
    # Capture video frame by frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera
cap.release()
cv2.destroyAllWindows()
