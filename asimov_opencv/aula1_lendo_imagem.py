import cv2

#Função imread

img = cv2.imread('assets/assets/fotos/cat.jpg')
img_large = cv2.imread('assets/assets/fotos/cat_large.jpg')
#Função imshow
cv2.imshow('Janela do gato', img_large)

#Função waitKey()
cv2.waitKey(0)


