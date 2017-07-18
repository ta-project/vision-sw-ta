import numpy as np
import cv2

font = cv2.FONT_HERSHEY_SIMPLEX
Car_cascade = cv2.CascadeClassifier('PrivateCarCascade.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    Car = Car_cascade.detectMultiScale(gray, 1.7,5,0,(200,200))     
    # add this
    for (x,y,w,h) in Car:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.putText(img,'Private Car',(x-int(w/16),y-int(h/16)), font, 1.0, (51,51,255), 2, cv2.LINE_AA)
        
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()