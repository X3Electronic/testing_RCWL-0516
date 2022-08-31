# Testing RCWL-0516
# Program by José Alfonso Suárez Moreno
# e-mail: alfonso.x3electronic@gmail.com

from machine import I2C, Pin
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
import utime


def main():
    # Dirección del I2C y tamaño del LCD
    I2C_ADDR = 0x27
    I2C_NUM_ROWS = 2
    I2C_NUM_COLS = 16

    # LCD Display I2C
    i2c = I2C(1, sda=Pin(14), scl=Pin(15), freq=400000)
    lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

    lcd.clear()

    rcwl_pin = Pin(17, Pin.IN)
    led_pin = Pin(25, Pin.OUT)
    time_start_on = utime.time()
    time_start_off = utime.time()
    print_off = False
    print_on = True

    while True:
        if rcwl_pin.value() == 1:
            if print_off:
                time_start_on = utime.time()
                elapsed_time_off = time_start_on - time_start_off
                lcd.move_to(0, 1)
                lcd.putstr('OFF .: ' + str(elapsed_time_off) + '   ')
                print_off = False
                print_on = True
            else:
                led_pin.on()
        else:
            if print_on:
                time_start_off = utime.time()
                elapsed_time_on = time_start_off - time_start_on
                lcd.move_to(0, 0)
                lcd.putstr('ON ..: ' + str(elapsed_time_on) + '   ')
                print_on = False
                print_off = True
            else:
                led_pin.off()


if __name__ == '__main__':
    main()
