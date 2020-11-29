import cv2
import sys
from mail import sending
from flask import Flask, render_template, Response
from camera import VideoCamera
import time
import threading
from call import call
from datetime import datetime
email_update_interval = 30 # sends an email only once in this time interval
video_camera = VideoCamera(flip=True) # creates a camera object, flip vertically
object_classifier = cv2.CascadeClassifier("models/fullbody_recognition_model.xml") # an opencv classifier

# App Globals (do not edit)
app = Flask(__name__)
last_epoch = 0

object_classifier = cv2.CascadeClassifier("models/fullbody_recognition_model.xml")
#jpeg,found_obj=video_camera.get_object()
#sending(jpeg)
def check_for_objects():
    while True:
        try:
            global last_epoch
            frame,found_obj=video_camera.get_object()
            if found_obj and (time.time()-last_epoch)>email_update_interval:
                last_epoch=time.time()
                call('+918465094927')
                sending(frame)
                print("all ok")
                now=datetime.now()
                current_time=now.strftime("%H:%M:%S")
                print(current_time)
        except:
            print("Error in sending email")
@app.route('/')
def index():
    return render_template('C:/Users/Teja/Desktop/hacker/files/index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--jpeg\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(video_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    t = threading.Thread(target=check_for_objects, args=())
    t.daemon = True
    t.start()
    app.run(host='0.0.0.0', debug=False)



    
