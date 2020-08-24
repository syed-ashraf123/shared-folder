import cv2 as cv
import face_recognition
import os
known=r'D:\Latestems\templates\known'
unknown=r'D:\Latestems\templates\unknown'
tolerance=0.6#If you make it hgher if you want recogntion very high.Default is around 0.6
#Real meaning= How much distance between faces to consider it a match. Lower is more strict. 0.6 is typical best performance.
frame=3
font=2
model="cnn"
known_faces=[]
known_names=[]

for name in os.listdir(known):
	for file in os.listdir(f"{known_faces}/{name}"):
		image=face_recognition.load_image_file(f"{known_faces}/{name}")
		encoding=face_recognition.face_encoding(image)[0]
		known_faces.append(encoding)
		known_names.append(names)
print("Processing")

for file in os.listdir(unknown):
	print(file)
	image=face_recognition.load_image_file(f"{unknown}/{file}")
	locations=face_recognition.face_locations(image,model=model)
	encoding=face_recognition.face_encoding(image,locations)
	image=cv.cvtColor(image,cv.COLOR_RGB2BGR)
	for face_encoding,face_location in zip(encoding,locations):
		results=face_recognition.compare_faces(known_faces,face_encoding,tolerance)
		match=None
		if True in results:
			match=known_names[results.index(True)]
			print(f"Match found: {match}")
			top_left=(face_locations[3],face_location[0])
			bottom_right=(face_location[1],face_location[2])
			color=[0,255,0]
			cv.rectangle(image,top_left,bottom_right,color,frame)
			top_left=(face_location[3],face_location[2])
			bottom_right=(face_location[1],face_location[2]+22)
			cv.rectangle(image,top_left,bottom_right,color,cv.FILLED)
			cv.putText(image, match, (face_location[3] + 10, face_location[2] + 15), cv.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200),font)
	cv.imshow(file,image)
	cv.waitKey(1000)
    #cv.destroyWindows(file)


