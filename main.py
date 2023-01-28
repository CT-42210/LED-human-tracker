import tensorflow as tf
import cv2

# Load TensorFlow Lite model
interpreter = tf.lite.Interpreter(model_path="lite-model_efficientdet_lite0_detection_default_1.tflite")
interpreter.allocate_tensors()

# Get input and output tensors
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# OpenCV video capture
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Pre-processing: resize and normalize
    frame = cv2.resize(frame, (320, 320))
    frame = frame / 255.0

    # Run inference
    interpreter.set_tensor(input_details[0]['index'], [frame])
    interpreter.invoke()
    boxes = interpreter.get_tensor(output_details[0]['index'])

    # Draw bounding boxes on the frame
    for box in boxes:
        xmin, ymin, xmax, ymax = box
        cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 0, 255), 2)

    # Display the resulting frame
    cv2.imshow('Human Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture
cap.release()
cv2.destroyAllWindows()
