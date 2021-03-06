# For this script you need a first "default" frame to set as a background.
# In situations with outdoor cameras,
# with lights changing quite constantly, this process
# results in a quite inflexible approach, so it is needed
# a bit more intelligence into the system


import cv2
import numpy as np

camera = cv2.VideoCapture(0)

es = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9,4))
kernel = np.ones((5,5), np.uint(8))
background = None

while(True):

    ret, frame = camera.read()
    if background is None:
        background = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # BGR color to GRAY if needed
        background = cv2.GaussianBlur(background, (31,31), 0)
        continue

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame, (31,31), 0)

    diff = cv2.absdiff(background, gray_frame)
    diff = cv2.threshold(diff, 20, 255, cv2.THRESH_BINARY)[1]
    diff = cv2.dilate(diff, es, iterations=4)
    image, cnts, hierarchy = cv2.findContours(diff.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    rectangle_number = 0
    for c in cnts:
        if cv2.contourArea(c) < 1500:
            continue
        (x,y,w,h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
        rectangle_number += 1

    print rectangle_number
    cv2.imshow("contours", frame)
    cv2.imshow("diff", diff)
    if cv2.waitKey(1000/12) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()
camera.release()