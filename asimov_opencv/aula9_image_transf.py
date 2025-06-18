import cv2
import numpy as np

img = cv2.imread('assets/assets/fotos/park.jpg')
cv2.imshow('Original', img)



def translate(img, x, y):
    
    translation_matrix = np.float32([[1, 0, x], [0, 1, y]])
    
    dimensions = (img.shape[1], img.shape[0])

    return cv2.warpAffine(img, translation_matrix, dimensions)

img_translated = translate(img, 100, 250)

cv2.imshow('Translated', img_translated)

cv2.waitKey(0)
