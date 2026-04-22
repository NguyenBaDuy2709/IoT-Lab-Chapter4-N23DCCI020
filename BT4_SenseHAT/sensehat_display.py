from sense_emu import SenseHat
import time
sense = SenseHat()
sense.show_message('hello IoT',text_colour=[0,185,0], scroll_speed=0.1)
time.sleep(1)
sense.clear()
print('text hien thi xong.')
