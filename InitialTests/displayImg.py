import cv2
import numpy as np

img = cv2.imread('randomgray.png')
cv2.imshow('Random Gray', img)
cv2.waitKey()
cv2.destroyAllWindows()