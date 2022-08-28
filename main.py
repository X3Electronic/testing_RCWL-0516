# Testing RCWL-0516
# Program by José Alfonso Suárez Moreno
# e-mail: alfonso.x3electronic@gmail.com

from machine import Pin
import utime


def main():
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
                print('Time OFF: ', elapsed_time_off)
                print_off = False
                print_on = True
            else:
                led_pin.on()
        else:
            if print_on:
                time_start_off = utime.time()
                elapsed_time_on = time_start_off - time_start_on
                print('Time ON: ', elapsed_time_on)
                print_on = False
                print_off = True
            else:
                led_pin.off()


if __name__ == '__main__':
    main()

