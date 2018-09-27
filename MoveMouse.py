# Prevent computer from sleeping

import pyautogui
import time
import random
import datetime



hours = int(input("\n \n Enter hours to move mouse: \n \n")) ## user enters hours to move mouse
repeatTime = hours*5
# waitmin = int(input("\n \n Enter minute intervals to move mouse: \n \n")) ## user enters mouse movement intervals
# sleeptime = waitmin*60 ## sleep time calc

x = 0
y = hours
print("\n Moving mouse for %s hours every 5 minutes... \n \n" % (hours))
# print("\n Moving mouse for %s hours every %s minutes... \n \n" % (hours,waitwin)) ## if user enters wait time
## Click mouse
for i in range(repeatTime):
        pyautogui.click(x=random.randint(400, 500), y=random.randint(400, 500), duration=1)
        print("Mouse last moved at %s - %s \n" % (time.strftime("%x"), time.strftime("%I:%M:%S %p"))) # display current time
        print("Running Time: %s hours \n" % str('{:04.2f}'.format(x/60)))
        print("Hours To Go: %s hours \n \n" % str('{:04.2f}'.format(y)))
        x += 5
        y -= 5/60
        time.sleep(300) ## 600 = move every 10 minutes, 300 = 5 minutes
        # time.sleep(sleeptime) ## if users enters minutes interval
        if x == repeatTime*5:
            print("Finished")
            break
        else:
            pass
        # move mouse to anywhere between 1 and 1000 pixel grid on screen
                    ## move 12 times X 5 minutes = 1 hours
                    ## move 24 times X 5 minutes = 2 hours
                    ## move 48 times X 5 minutes = 4 hours


## Move mouse
# pyautogui.moveTo(random.randint(1, 1000), random.randint(1, 1000), duration=3)

## Click mouse
# pyautogui.click(x=random.randint(400, 500), y=random.randint(400, 500), duration=1)
