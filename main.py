from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics
import datetime

Screen_Width = GetSystemMetrics(0)
Screen_Height = GetSystemMetrics(1)
Time_Stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
print(Time_Stamp)
Fila_Name = f"Recording {Time_Stamp}.mp4"
Fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
Captured_Video = cv2.VideoWriter(Fila_Name, Fourcc, 20.0, (Screen_Width, Screen_Height))

while True:
    Img = ImageGrab.grab(bbox=(0, 0, Screen_Width, Screen_Height))
    Img_Np = np.array(Img)
    Img_Final = cv2.cvtColor(Img_Np, cv2.COLOR_BGR2RGB)
    cv2.imshow('Secret Capture', Img_Final)
    Captured_Video.write(Img_Final)
    if cv2.waitKey(10) == ord('q') or cv2.waitKey(10) == ord():
        break
    cv2.destroyAllWindows()
