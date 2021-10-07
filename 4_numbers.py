from machine import Pin, SoftI2C
import time
from ssd1306 import SSD1306_I2C
import machine
import math

i2c = SoftI2C(scl=Pin(4), sda=Pin(5))
oled = SSD1306_I2C(128, 64, i2c)

for i in range(51):
    oled.fill(0)
    oled.text(str(i), 10, 10)
    oled.text(str(math.sqrt(i)), 10, 50)
    oled.text(str(50-i), 100, 10)
    oled.text(str(i-50), 100, 50)
    

    oled.show()
    time.sleep(1)