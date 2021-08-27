
import cv2

# start recording a video - "0" is your default webcam
video = cv2.VideoCapture(0)

# chech if camera is working correctly

if not video.isOpened():
    raise IOError('Camera is not working properly')

while True:

    ret, frame = video.read()
    frame = cv2.resize(frame, None, fx=1, fy=1, interpolation=cv2.INTER_AREA)

    cv2.imshow('Test frame', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):                
        break

video.release()
cv2.destroyAllWindows()  


