import cv2
import numpy as np



# RGB -> praticamente o padrão
# BGR -> OpenCV usa esse padrão
# CMYK -> usado na impressão

img = cv2.imread('assets/assets/fotos/cat.jpg')



gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', hsv)

lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow('LAB', lab)

cv2.waitKey(0)
