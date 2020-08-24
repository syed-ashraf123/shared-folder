import cv2
import face_recognition
import pandas as pd

img = face_recognition.load_image_file('IMG_20200222_162416.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

 
faceLoc = face_recognition.face_locations(img)[0]
encode = face_recognition.face_encodings(img)[0]

df=pd.DataFrame({"Osama":encode})
df.to_csv('data.csv')