from tabnanny import check
import cv2
from matplotlib import ticker

#import video or open webcam
cap = cv2.VideoCapture("Mark.mp4")# Change the video name to number for webcam (0 for default webcam, 1,2,3,... for external webcam)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #import the haarcascade_frontalface_default.xml
#? haarcascade_frontalface_default.xml is face detection file.

#show video
while (cap.isOpened()): #while video is open
    check, frame = cap.read() #read video
    if(check == True):#check if video has next frame.
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #convert to grayscale
        face_detect  = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5) #detect face, scaleFactor is the scale of the image, minNeighbors is the number of neighbors
        for (x, y, w, h) in face_detect: #for each face detected
            #cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), thickness=3) #draw rectangle around face
            frame[y:y+h+30, x:x+w+30] = cv2.blur(frame[y:y+h+30, x:x+w+30], (50,50)) #blur the face
            cv2.imshow("Video", frame) #show video
        if cv2.waitKey(1) & 0xFF == ord('q'): #if q is pressed, break
            break
    
    else:
        break

cap.release() #release video
cv2.destroyAllWindows() #close all windows and give memory back to computer