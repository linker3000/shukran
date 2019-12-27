"""

  V1.0 Linker3000 (Nigel Kendrick) December 2019.
  
  Released into the public domain 'as is'.
  
  This is an unsupported program, but error reports and suggestions
  for improvement are welcome. linker3000-at-gmail.com. 
  
  A simple 'blink' program for testing FT232H/Shukran board
  functionality.
  
  See: https://github.com/linker3000/shukran
  
  Requires FT232H/USB drivers and CircuitPython installed - see
  https://learn.adafruit.com/circuitpython-on-any-computer-with-ft232h
  
  The default programming below alternately flashes the LEDs
  connected to FT232H pins C3 and C4 on the CJMCU FT232H board as an 
  initial connectivity and setup test.
  
  To test the Shukran board, try jumpering its user LEDs to a pair
  of port header pins on H1 and adjusting the program to use them.  
  
  NOTES:
  
  FT232H pins C8 and C9 cannot be controlled by digital I/O code 
  and trying to use them here will result in a program error.
  
  The CircuitPython code and libraries are written for python3, so
  to run this program, type: python3 ft232blink.py. If you forget the
  '3' and this runs the program with python2, you will most likely
  see the error message "ImportError: No module named board".

  If following the CircuitPython blinka setup notes, remember to set
  the BLINKA_FT232H environment variable.
 
  Happy hacking!
  
"""

import time
import board
import digitalio
     
led = digitalio.DigitalInOut(board.C3)
led.direction = digitalio.Direction.OUTPUT
     
led2 = digitalio.DigitalInOut(board.C4)
led2.direction = digitalio.Direction.OUTPUT
     
while True:
    led.value = True
    led2.value = False
    time.sleep(0.5)
    led.value = False
    led2.value = True
    time.sleep(0.5)

