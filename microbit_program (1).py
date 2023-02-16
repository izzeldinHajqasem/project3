# Add your Python code here. E.g.
from microbit import *
import radio
radio.config(group=7)
radio.on()
while True:
    temp = temperature()
    if temp>=27:
        radio.send("high")
    else:
        radio.send("low")
    