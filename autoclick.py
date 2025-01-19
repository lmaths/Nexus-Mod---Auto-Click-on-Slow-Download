import pyautogui
import time

INTERVALO = 10

while True:
    try:
        button_location = pyautogui.locateCenterOnScreen('slow_download.png', confidence=0.8)
        
        if button_location:
            pyautogui.click(button_location)
            print(f"Botão clicado em {button_location}")
        else:
            print("Botão não encontrado na tela!")

    except Exception as e:
        print(f"Erro: {e}")

    time.sleep(INTERVALO)
