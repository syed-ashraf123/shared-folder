import cv2 as cv
import cv2
import face_recognition
import time
cap=cv.VideoCapture(0)
cap.set(3,1208)
cap.set(4,720)
#img=face_recognition.load_image_file('known/osama/IMG_20200222_162416.jpg')
#img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
#faceloc=face_recognition.face_locations(img)[0]

#imgencode=face_recognition.face_encodings(img)[0]
a=1
while (cap.isOpened()):
	ret,frame=cap.read()
	if a:
		time.sleep(15)
	faceloc=face_recognition.face_locations(frame)[0]
	a=0
	cv.rectangle(frame,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(255,0,255),2)
	cv.imshow("Frame",frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break



#results=face_recognition.face_locations(imgtest)

cap.release()
cv.destroyAllWindows()