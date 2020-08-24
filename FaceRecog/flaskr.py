# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 18:57:44 2019
@author: seraj
"""
import numpy as np
import pandas as pd
df=pd.read_csv('data.csv')
z=[]
for i in range(2):
	if i==0:
		continue
		z.append(np.array(df.iloc[:,i]))

import time

import cv2 
from flask import Flask, render_template, Response
import cv2 as cv
import cv2
import face_recognition
import pandas as pd
df=pd.read_csv('data.csv')

app = Flask(__name__)

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen():
    """Video streaming generator function."""
    cap = cv2.VideoCapture(0)

    # Read until video is completed
    while(cap.isOpened()):
      # Capture frame-by-frame
        ret, img = cap.read()
        if ret == True:
        	try:
	        	faceloc=face_recognition.face_locations(img)[0]
	        	cv.rectangle(img,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(255,0,255),2)
	        	encodedcurr = face_recognition.face_encodings(img)[0]
	        	facedis=face_recognition.face_distance(z,encodedcurr)
	        	print(facedis)
	        	img = cv2.resize(img, (0,0), fx=0.5, fy=0.5) 
	        	frame = cv2.imencode('.jpg', img)[1].tobytes()

	        	yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
	        	time.sleep(0.1)
	        except:
	        	print("except")
	        	img = cv2.resize(img, (0,0), fx=0.5, fy=0.5) 
	        	frame = cv2.imencode('.jpg', img)[1].tobytes()
	        	yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
	        	time.sleep(0.1)	        	
        else:
        	break
        

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

