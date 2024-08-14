from microbit import *
import maqueenplus
from time import sleep_ms

# Initialise the MaqueenPlus robot
# If it's successful, you should see the robot version number (1.4) scroll
# across the Microbit, and it will then show a tick
mq = maqueenplus.MaqueenPlus(pin1, pin2)
Arden = False
while True:
    if pin_logo.is_touched():
        Arden = True

    if Arden == True:
        display.show("S")
        mq.set_headlight_rgb(mq.HEADLIGHT_BOTH, mq.COLOR_BLUE)
        sleep_ms(1000)
        display.show("B")
        mq.set_headlight_rgb(mq.HEADLIGHT_BOTH, mq.COLOR_RED)
        sleep_ms(1000)
        display.show("J")
        mq.set_headlight_rgb(mq.HEADLIGHT_BOTH, mq.COLOR_YELLOW)
        sleep_ms(1000)
        if button_a.is_pressed():
            Arden = False
            display.clear()
            mq.set_headlight_rgb(mq.HEADLIGHT_BOTH, mq.COLOR_OFF)
        


# Advanced:
#
# Your code probably takes up to 3 seconds to respond to the press of
# button A - that is, it goes through all three houses before it stops.
# Can you improve the responsiveness so it will respond within 1 second,
# that is, stop after the current house?
#
# Can you improve it to be better than 1 second?
#
