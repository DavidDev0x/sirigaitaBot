import pyautogui
import cv2
import numpy as np
from pynput.mouse import Listener

def selecionar_area_por_clique():
    pontos = []

    def on_click(x, y, button, pressed):
        if pressed:
            pontos.append((x, y))
            if len(pontos) == 2:
                return False

    with Listener(on_click=on_click) as listener:
        listener.join()

    (x1, y1), (x2, y2) = pontos
    x = min(x1, x2)
    y = min(y1, y2)
    w = abs(x2 - x1)
    h = abs(y2 - y1)
    return (x, y, w, h)

def capturar_area(area):
    shot = pyautogui.screenshot(region=area)
    frame = np.array(shot)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return gray
