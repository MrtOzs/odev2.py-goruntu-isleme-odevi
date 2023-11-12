import cv2
import numpy as nump

kamera = cv2.VideoCapture(0)
while True:
    x, cerceve = kamera.read()
    hsvgecis = cv2.cvtColor(cerceve, cv2.COLOR_BGR2HSV)
    altkirmizi = nump.array([0, 100, 45])
    ustkirmizi = nump.array([10, 255, 255])
    maske = cv2.inRange(hsvgecis, altkirmizi, ustkirmizi)
    a = cv2.bitwise_and(cerceve, cerceve, mask=maske)
    cv2.imshow('cerceve', cerceve)
    cv2.imshow('a', a)
    if cv2.waitKey(1) & 0xFF == ord('i'):
        break
kamera.release()
cv2.destroyAllWindows()