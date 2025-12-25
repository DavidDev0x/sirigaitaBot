import time
import cv2
import threading
from screen import capturar_area
from actions import executar_combo

THRESHOLD = 0.92     # ajuste fino
COOLDOWN = 3         # segundos

class PokemonBot:
    def __init__(self):
        self.running = threading.Event()
        self.ultimo_ataque = 0

    def iniciar(self, area, img_base_gray, hotkeys):
        self.running.set()
        base = img_base_gray

        while self.running.is_set():
            atual = capturar_area(area)
            if atual is None:
                time.sleep(0.2)
                continue

            res = cv2.matchTemplate(atual, base, cv2.TM_CCOEFF_NORMED)
            _, similaridade, _, _ = cv2.minMaxLoc(res)

            # DEBUG (opcional)
            print(f"similaridade: {similaridade:.3f}")

            if similaridade < THRESHOLD:
                agora = time.time()
                if agora - self.ultimo_ataque >= COOLDOWN:
                    print(">>> ATACANDO <<<")
                    executar_combo(hotkeys)
                    self.ultimo_ataque = agora

            time.sleep(0.15)

    def parar(self):
        self.running.clear()
