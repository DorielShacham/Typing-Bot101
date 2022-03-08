#CREATED BY DORIEL SHACHAM ENJOY - JUST RUN THIS AND YOU GOT 5 SECONDS TO CLICK SOMEWHERE ELSE BUT HERE
#Import modules
import pyautogui
import time
pyautogui.FAILSAFE = True
time.sleep(5) #Python files sleeps for 5 seconds
text = open("text.txt.txt") #Opening the txt file
for each_line in text:
    pyautogui.typewrite(each_line) #this is if we make break lines in our txt file