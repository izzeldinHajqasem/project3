# Add your Python code here. E.g.
from microbit import *
import radio
radio.config(group=7)
radio.on()
while True:
   temp =  radio.receive()
   if temp == "high":
        pin0.write_digital(0)
        display.scroll("i")
   elif temp == "low":
        pin0.write_digital(1)
