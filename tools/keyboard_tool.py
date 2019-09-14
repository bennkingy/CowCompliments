import pyautogui
import time

def bot_speak(msg):
    pyautogui.typewrite(msg, interval=0.10)
    pyautogui.press('enter')  # press the Enter key 

def main():

    # Open the file and read the contents
    f=open("cow_compliments.py", "r")
    fl =f.readlines()
    for x in fl:
        pyautogui.typewrite(x, interval=0.01)

if __name__== "__main__":
    time.sleep(10)
    main()