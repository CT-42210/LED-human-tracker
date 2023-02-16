import cv2

camera = cv2.VideoCapture(1)

camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

ret, frame = camera.read()

num = 1
while True:
    cv2.rotate(frame, cv2.ROTATE_180)
    cv2.imshow('img1', frame)
    if cv2.waitKey(1) & 0xFF == ord('y'):
        cv2.imwrite(f'/Desktop/test-images/c{num}.png', frame)
        num = num + 1

    if cv2.waitkey(1) == ord('q'):
        cv2.destroyAllWindows()
        break

camera.release()
