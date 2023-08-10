from machine import Pin, I2C, ADC, PWM
from ssd1306 import SSD1306_I2C
import framebuf,sys,time
import utime


sensor = machine.ADC(28)
threshold = 1000 #This value needs to be modified with the environment.

pix_res_x  = 128 # SSD1306 horizontal resolution
pix_res_y = 64   # SSD1306 vertical resolution
i2c_dev = I2C(1,scl=Pin(27),sda=Pin(26),freq=200000)  # start I2C on I2C1 (GPIO 26/27)
i2c_addr = [hex(ii) for ii in i2c_dev.scan()] # get I2C address in hex format
oled = SSD1306_I2C(pix_res_x, pix_res_y, i2c_dev) # oled controller

adc_2 = machine.ADC(2) # ADC channel 2 for input

buzzer = PWM(Pin(15))
buzzer.freq(500)
while True:
    value=sensor.read_u16()
    if value > threshold :
        oled.fill(0) # clear the display
        oled.text("water",0 ,0)
        oled.show() # show the new text and image
       
    else:
        oled.fill(0) # clear the display
        oled.text("no water",0 ,0)
        oled.show()
        buzzer.duty_u16(0)
    if value > threshold:
        buzzer.duty_u16(1000)
        utime.sleep(.5)
        buzzer.duty_u16(0)
        utime.sleep(.1)
    utime.sleep_ms(5)
