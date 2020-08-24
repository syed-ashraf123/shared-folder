# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 18:57:44 2019
@author: seraj
"""
import numpy as np
import cv2
import pandas as pd
import face_recognition
df=pd.read_csv('data.csv')
z=[]
for i in range(2):
	if i==0:
		continue
	z.append(np.array(df.iloc[:,i]))


cap = cv2.VideoCapture(0)
cap.set(3,1208)#Setting window width to 1208 and 3 is telling we're calling width
cap.set(4,720)

# Read until video is completed
while 1:

  # Capture frame-by-frame
    ret, img = cap.read()
    try:
        #faceloc=face_recognition.face_locations(img)[0]
        #cv2.rectangle(img,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(255,0,255),2)
        #encodedcurr = face_recognition.face_encodings(img)[0]
        #facedis=face_recognition.face_distance(z,encodedcurr)
        #results = face_recognition.compare_faces(z,encodedcurr)
        #print(facedis,results)
        cv2.imshow("Frame",img)
        if cv2.waitKey(1) & 0xFF == ord('q'): #Will wait for our key q to be pressed
            break
    except:
        cv2.imshow("Frame",img)
cap.release()