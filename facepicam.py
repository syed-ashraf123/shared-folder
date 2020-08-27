y1,x2,y2,x1=0,0,0,0
from flask_opencv_streamer.streamer import Streamer
port = 3030
require_login = False
streamer = Streamer(port, require_login)
import cv2
import multiprocessing
from flask import Flask, render_template, Response

from multiprocessing import Queue
Q=Queue()
import pandas as pd
import numpy as np
from scipy.misc import toimage
from PIL import Image
from gpiozero import LED
led=LED(17)
a=True
df=pd.read_csv('data.csv')
z=[]
for i in range(2):
    if i==0:
        continue
    z.append(np.array(df.iloc[:,i]))
import picamera
import pyrebase
config={
"apiKey": "AIzaSyBN0Ej4ge3rEiIKe04SCC4MAgWtKBnqwb4",
    "authDomain": "security-266e5.firebaseapp.com",
    "databaseURL": "https://security-266e5.firebaseio.com",
    "projectId": "security-266e5",
    "storageBucket": "security-266e5.appspot.com",
    "messagingSenderId": "597325357058",
    "appId": "1:597325357058:web:c0919ec2bc99f47b9c871b"
}
#firebase=pyrebase.initialize_app(config)
#storage=firebase.storage()
import png
import scipy.misc
import picamera.array
import face_recognition

app = Flask(__name__)

with picamera.PiCamera() as camera:
    with picamera.array.PiRGBArray(camera) as stream:
        camera.resolution = (600, 400)
        camera.vflip=True


        while True:
            camera.capture(stream, 'bgr', use_video_port=True)
            frameS=cv2.resize(stream.array,(0,0),None,0.25,0.25)
            frameS=cv2.cvtColor(frameS,cv2.COLOR_BGR2RGB)
            if face_recognition.face_locations(frameS):
                led.on()
                y1,x2,y2,x1=face_recognition.face_locations(frameS)[0]
                encodeTest = face_recognition.face_encodings(frameS)[0]
                result=face_recognition.compare_faces(z,encodeTest,0.6)
                y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(stream.array,(x1,y1),(x2,y2),(255,0,255),2)
                if result[0]==True:
                    cv2.putText(stream.array,"Known",(x1-6,y2+6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                else:
                    print("Onknown")
                    cv2.putText(stream.array,"Unknown",(x1-6,y2+6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                    #cv2.imwrite("/home/pi/Downloads/shared-folder-master/FaceRecog/frame20sec.jpg", frameS)
                    #storage.child("images/unk2.jpeg").put(np.asarray(frameS.tolist(), dtype=np.uint8))

            else:
                led.off()
            #cv2.imshow('frame', stream.array)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            # reset the stream before the next capture
            stream.seek(0)
            stream.truncate()

        cv2.destroyAllWindows()