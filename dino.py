import pyautogui
from PIL import Image, ImageGrab
import time

    for i in range(300, 415):
        for j in range(563, 650):
            if key[i, j] < 100:
                pyautogui.keyDown("up")
                return

    return

if __name__ == '__main__':
    print("Hey... Dino game about to start in 3 seconds...")
    time.sleep(3)
    # pyautogui.keyDown("up")
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        jump(data)
        
