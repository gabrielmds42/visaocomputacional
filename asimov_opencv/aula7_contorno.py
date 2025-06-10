import cv2
import numpy as np

img = cv2.imread('assets/assets/fotos/cats.jpg')
cv2.imshow('Cats', img)


blank = np.zeros(img.shape, dtype='uint8')


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



blur = cv2.GaussianBlur(gray, (5,5), cv2.BORDER_DEFAULT)
cv2.imshow('blur', blur)

canny = cv2.Canny(blur, 125, 175)
cv2.imshow('canny', canny)

contornos, hier = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print(f'{len(contornos)} contornos foram encontrados!')

cv2.drawContours(blank, contornos, -1, (0,0,255), 1)
cv2.imshow('contornos desenhados', blank)
cv2.waitKey(0)
