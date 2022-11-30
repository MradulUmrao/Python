#importing modules
import time
import pyautogui
#input program
message = input("Enter your Message:")
time3 = float(input("Enter time in seconds you need to reach where ever you want to reach:"))

#main  program
time.sleep(time3)

i=0
while i<=0:
    pyautogui.typewrite(message)
    pyautogui.press("enter")
