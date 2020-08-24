import cv2 as cv
cap=cv.VideoCapture(0)
cv.namedWindow("Tracking")#A window for tracking objects or hsv values correctly.
cv.createTrackbar('LH','Tracking',0,255,nothing)#Lower hue
cv.createTrackbar('LS','Tracking',0,255,nothing)#0.255 got color space but i think it can be increased as it is a hsv or maybe not.Don't focus much
cv.createTrackbar('LV','Tracking',0,255,nothing)#Lower Value
cv.createTrackbar('UH','Tracking',255,255,nothing)
cv.createTrackbar('US','Tracking',255,255,nothing)#Upper Saturatiion
cv.createTrackbar('UV','Tracking',255,255,nothing)
while 1:
    #frame=cv.imread('smarties.png')
    _,frmae=cap.read()
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)#Converting to HSV to get color number
    
    l_h=cv.getTrackbarPos('LH','Tracking')
    l_s=cv.getTrackbarPos('LS','Tracking')
    l_v=cv.getTrackbarPos('LV','Tracking')
    
    u_h=cv.getTrackbarPos('UH','Tracking')
    u_s=cv.getTrackbarPos('US','Tracking')
    u_v=cv.getTrackbarPos('UV','Tracking')
    
    l_b=np.array([l_h,l_s,l_v])#Lower bound/You know maybe its cylinderical
    u_b=np.array([u_h,u_s,u_v])#uppar bound
    mask=cv.inRange(hsv,l_b,u_b)#making a threshhold to get above color or object only.
    res=cv.bitwise_and(frame,frame,mask=mask)#Doing the AND operation so,it will only match mask color or object in a frame which matches the above mask
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    key=cv.waitKey(1)
    if key==27:
        break
cap.release()
cv.destroyAllWindows()