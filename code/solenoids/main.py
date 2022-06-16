import gpiozero
import time

outpin = 14

led = gpiozero.LED(outpin)

while True:
    print("on")
    led.on()
    time.sleep(1)
    print("off")
    led.off()
    time.sleep(1)
