import cv2
import time
import numpy as np
from mail import sending

def check_objects():
    faceDetect=cv2.CascadeClassifier("C:/opencv/haarcascade_frontalface_default.xml")
    cam=cv2.VideoCapture(0)
    time.sleep(2.0)
    update_interval=30
    #id=input("entera number")
    sampleNum=0
    found_obj=False
    while True:
        found_obj=False
        ret,frame=cam.read()
        if len(frame)>1:
            found_obj=True
        faces=faceDetect.detectMultiScale(frame,1.3,5)
        sampleNum=sampleNum+1
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        frame1=cv2.imencode(".jpeg",frame)[1].tostring()
        cv2.imshow("frame",frame)
        cv2.waitKey(20)
        if sampleNum==1:
            break
        return (frame1,found_obj)
    cam.release()
    cv2.destroyAllWindows()
update_interval=30
last_epoch=0
def check():
    update_interval=30
    frame1,found_obj=check_objects()
    global last_epoch
    if found_obj and (time.time()-last_epoch)>update_interval:
        last_epoch=time.time()
        sending(frame1)
        print("all ok")
    else:
         print("not ok")
check()