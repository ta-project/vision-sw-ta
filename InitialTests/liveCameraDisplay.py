import cv2


cameraCapture = cv2.VideoCapture(0)
cv2.namedWindow('Window1')

print 'Showing camera feed. Click window or press any key to stop.'
success, frame = cameraCapture.read()
key = False

while success and not key:
    key = cv2.waitKey(1) == 27  #esc key pressed
    cv2.imshow('Window1', frame)
    success, frame = cameraCapture.read()


cv2.destroyWindow('MyWindow')
cameraCapture.release()