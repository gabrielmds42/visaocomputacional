import cv2
import numpy as np

cap = cv2.VideoCapture(2)


while True:
    _, frame = cap.read()

    cv2.imshow('Gravando e testando', frame)

    if cv2.waitKey(20) & 0xFF==ord('d'):
        break
