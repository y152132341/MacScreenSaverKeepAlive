import time
import sys
import pyautogui

try:
	while True:
		x, y = pyautogui.position()
		pyautogui.moveTo(x+1, y+1)
		pyautogui.moveTo(x, y)
		time.sleep(110)
except KeyboardInterrupt:
	sys.exit()
