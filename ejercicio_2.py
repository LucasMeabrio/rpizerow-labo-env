from gpiozero import LED
from time import sleep
import threading

# Definir los pines GPIO para cada color del LED RGB
rojo_led = LED(17)  
azul_led = LED(27)
verde_led = LED(22)

# Función para hacer parpadear los LEDs según el intervalo especificado
def alternar(led, delay): 
    while True:
        led.on()
        sleep(delay)
        led.off()
        sleep(delay)

# Crear hilos para cada LED con su intervalo específico
hilo_rojo = threading.Thread(target=alternar, args=(rojo_led, 1))
hilo_azul = threading.Thread(target=alternar, args=(azul_led, 0.5))
hilo_verde = threading.Thread(target=alternar, args=(verde_led, 0.25))

# Iniciar los hilos
hilo_rojo.start()
hilo_azul.start()
hilo_verde.start()

# Mantener el programa en ejecución para que los hilos continúen ejecutándose
hilo_rojo.join()
hilo_azul.join()
hilo_verde.join()
