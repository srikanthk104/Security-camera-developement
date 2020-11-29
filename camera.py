import cv2
import cv2
import imutils
import time
import numpy as np
import mail
classifier=cv2.CascadeClassifier("C:/opencv/haarcascade_frontalface_default.xml")

class VideoCamera():
    def __init__(self,flip=False):
        self.cam=cv2.VideoCapture(0)
        self.flip=flip
        time.sleep(2.0)
    def flip_if_needed(self,frame):
        if self.flip:
                return np.flip(frame,0)
        return frame
    
    def get_frame(self):
        classifier=cv2.CascadeClassifier("C:/opencv/haarcascade_frontalface_default.xml")
        while True:
            ret,frame = self.flip_if_needed(self.cam.read())
            jpeg = cv2.imencode('.jpg', frame)[1].tostring()
        return jpeg
        self.cam.release()
        cv2.destroyAllWindows()
    def get_object(self):
        found_objects=False
        sampleNum=0
        classifier=cv2.CascadeClassifier("C:/opencv/haarcascade_frontalface_default.xml")
        while True:
            ret,frame= self.cam.read()
            gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
            objects = classifier.detectMultiScale(gray,1.3,5)
            sampleNum=sampleNum+1
            if len(objects) > 0:
                     found_objects = True
            for (x, y, w, h) in objects:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.imshow("frame",frame)
            jpeg = cv2.imencode('.jpg', frame)[1].tostring()
            if sampleNum==1:
                break
            cv2.waitKey(10)
        return (jpeg, found_objects)
        self.cam.release()
        cv2.destroyAllWindows()