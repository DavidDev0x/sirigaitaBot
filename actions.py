import pyautogui
import time

def executar_combo(hotkeys):
    pyautogui.press(hotkeys["target"])
    pyautogui.press(hotkeys["buff"])
    pyautogui.press(hotkeys["attack"])
    pyautogui.press(hotkeys["heal"])
