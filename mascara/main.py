import cv2
import mediapipe as mp
import numpy as np

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

mask = cv2.imread('vecteezy_a-black-mask-with-a-black-face_48719161.png', cv2.IMREAD_UNCHANGED)

if mask is None:
    raise ValueError("Erro: não foi possível carregar a imagem da máscara.")

cap = cv2.VideoCapture(2)

with mp_face_detection.FaceDetection(min_detection_confidence=0.7) as face_detection:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_detection.process(image)

        if results.detections:
            for detection in results.detections:
                bbox = detection.location_data.relative_bounding_box
                h, w, _ = frame.shape
                x = int(bbox.xmin * w)
                y = int(bbox.ymin * h)
                w_box = int(bbox.width * w)
                h_box = int(bbox.height * h)

                # Correção: manter dentro dos limites da imagem
                x = max(0, x)
                y = max(0, y)
                w_box = min(w_box, w - x)
                h_box = min(h_box, h - y)

                if w_box <= 0 or h_box <= 0:
                    continue

                mask_resized = cv2.resize(mask, (w_box, h_box))

                roi = frame[y:y+h_box, x:x+w_box]

                mask_rgb = mask_resized[:, :, :3]
                mask_alpha = mask_resized[:, :, 3] / 255.0

                for c in range(3):
                    roi[:, :, c] = roi[:, :, c] * (1 - mask_alpha) + mask_rgb[:, :, c] * mask_alpha

                frame[y:y+h_box, x:x+w_box] = roi

        cv2.imshow('Mascara na Face', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

