import cv2

camera = cv2.VideoCapture(0)

camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

with open("c-count", "r") as c_read:
    c_num = c_read.read()

while True:
    ret, frame = camera.read()

    cv2.rotate(frame, cv2.ROTATE_180)
    cv2.imshow('img1', frame)

    if cv2.waitKey(1) & 0xFF == ord('y'):
        cv2.imwrite(f'/home/pi/Desktop/test-images/c{c_num}.png', frame)
        c_num = c_num + 1
        with open("c-count", "w") as c_write:
            c_read.write(c_num)

    elif cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break

camera.release()
