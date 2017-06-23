import cv2
import numpy as np

bs = cv2.createBackgroundSubtractorKNN(detectShadows=True)
camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    foreground_mask = bs.apply(frame)
    th = cv2.threshold(foreground_mask.copy(), 244, 255, cv2.THRESH_BINARY)[1]
    dilated = cv2.dilate(th, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3)), iterations=2)
    image, contours, hier = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) > 1600:
            (x,y,w,h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255,255,0), 2)

    cv2.imshow("mog", foreground_mask)
    cv2.imshow("thresh", th)
    cv2.imshow("detection", frame)
    if cv2.waitKey(30) & 0xff == 27:
        break

camera.release()#ss
cv2.destroyAllWindows()