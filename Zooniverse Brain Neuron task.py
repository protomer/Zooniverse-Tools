import pyautogui
import numpy as np
import time

hex_color = '#EBEBEB'  # Replace with your hex
rgb = tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))

screenshot = pyautogui.screenshot()
img = np.array(screenshot)

mask = (img[:,:,0] == rgb[0]) & (img[:,:,1] == rgb[1]) & (img[:,:,2] == rgb[2])
positions = np.argwhere(mask)

if len(positions) > 0:
    y, x = positions[0]
    time.sleep(3)
    pyautogui.click(x, y)