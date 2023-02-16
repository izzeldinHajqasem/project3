# Add your Python code here. E.g.
from microbit import *


while True:
    temp = temperature()
    if temp >= 25:
        pin0.write_digital(0)
    else:
        pin0.write_digital(1)
    display.scroll(str(temp))
    