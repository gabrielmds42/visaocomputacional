import cv2
import numpy as np


img = cv2.imread('assets/assets/fotos/cat.jpg')
img2 = cv2.imread('assets/assets/fotos/park.jpg')



cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow('gatito', img)
#cv2.imshow('gatito cinza', cinza)
#cv2.waitKey(0)

blurred = cv2.GaussianBlur(img, (3,3), cv2.BORDER_DEFAULT)
#cv2.imshow('blurred', blurred)


canny = cv2.Canny(img, 250, 200)
#cv2.imshow('canny_normal', canny)

canny_blurred = cv2.Canny(blurred, 250, 200)

#cv2.imshow('canny_blurred', canny_blurred)


dilatada = cv2.dilate(canny_blurred, (9,9), iterations=3)
#cv2.imshow('dilatada', dilatada)

eroded = cv2.erode(dilatada, (9,9), iterations=3)
cv2.imshow('eroded', eroded)
resized = cv2.resize(img, (300, 300))

#cv2.imshow('resized', resized)

corte = img[50:200, 200:400]
cv2.imshow('corte', corte)
cv2.waitKey(0)
