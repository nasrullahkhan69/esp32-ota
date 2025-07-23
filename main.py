from machine import Pin
import time

led = Pin(2, Pin.OUT)  # Built-in LED on GPIO2

while True:
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(3)
