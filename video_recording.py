
import cv2
import sys

# cascades are necessary to recognise face and smile properly
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') 
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml') 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# this function recognizes a smile and saves the photo on HDD
def happy_selfie(gray, frame): 
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    '''
    # place rectangles on face
    for (x, y, w, h) in faces: 
        cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (255, 0, 0), 0) 
        roi_gray = gray[y:y + h, x:x + w] 
        roi_color = frame[y:y + h, x:x + w] 
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20) 
  
        # place rectangles on smile
        for (sx, sy, sw, sh) in smiles: 
            cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 0)
            
            count=0
            # save a picture on disk
            cv2.imwrite('Snapshot '+str(count)+'.jpg', smiles)
            count+=1
            if count>=5:
                break'''
    return frame

# start recording a video - "0" is your default webcam
video = cv2.VideoCapture(0)

# loop is necessary, because video is an "endless slideshow"
while True: 

   # captures video_capture frame by frame 
    _, frame = video.read()  
  
    # To capture image in monochrome                     
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   
      
    # calls the HappySelfie() function     
    smile = happy_selfie(gray, frame)    
  
    # displays the result on camera feed                      
    cv2.imshow('Test Frame', smile)
 
    # press q to quit                         
    if cv2.waitKey(1) & 0xff == ord('q'):                
        break
  
# Release the capture once all the processing is done. 
video.release()                                  
cv2.destroyAllWindows()  


