import cv2

camera = cv2.VideoCapture(0)
ret,frame = camera.read()

while(True):
    cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    cv2.imshow('img1',frame)
    if cv2.waitKey(1) & 0xFF == ord('y'):
        cv2.imwrite('c1.png',frame)
        cv2.destroyAllWindows()
        break

camera.release()
