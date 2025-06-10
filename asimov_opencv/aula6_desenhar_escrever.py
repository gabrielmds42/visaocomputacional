import cv2
import numpy as np


azul = 255, 0 , 0
verde = 0, 255, 0
vermelho = 0, 0, 255


#blank = np.zeros((500, 500), dtype='uint8')

blank_img = np.zeros((500, 500, 3), dtype='uint8')

cat = cv2.imread('assets/assets/fotos/cat.jpg')


#blank_img[:] = vermelho
#blank_img[:] = verde
#blank_img[:] = azul

cv2.imshow('blank', blank_img)

cv2.waitKey(0)
