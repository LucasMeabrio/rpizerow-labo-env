from gpiozero import LED
from time import sleep
import threading

rojo_led = LED(17)  
azul_led = LED(27)
verde_led = LED(22)

def alternar(led, delay): 
    while True:
        led.on()
        sleep(delay)
        led.off()
        sleep(delay)

hilo_rojo = threading.Thread(target=alternar, args=(rojo_led, 1))
hilo_azul = threading.Thread(target=alternar, args=(azul_led, 0.5))
hilo_verde = threading.Thread(target=alternar, args=(verde_led, 0.25))

hilo_rojo.start()
hilo_azul.start()
hilo_verde.start()

hilo_rojo.join()
hilo_azul.join()
hilo_verde.join()
