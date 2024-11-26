import time
from gpiozero import PWMLED
from Adafruit_ADS1x15 import ADS1115

led_rojo = PWMLED(17)
led_azul = PWMLED(27)

adc = ADS1115()

GAIN = 1

def leer_potenciometro():
    valor_adc = adc.read_adc(0, gain=GAIN)
    temperatura_pot = valor_adc * 30.0 / 32767.0
    return temperatura_pot

def leer_termistor():
    valor_adc = adc.read_adc(1, gain=GAIN)
    temperatura_real = valor_adc * 30.0 / 32767.0
    return temperatura_real

def control_proporcional():
    while True:
        temperatura_pot = leer_potenciometro()
        temperatura_real = leer_termistor()
        diferencia = temperatura_real - temperatura_pot

        if diferencia > 0:
            brillo_azul = min(diferencia / 5.0, 1.0)
            led_azul.value = brillo_azul
            led_rojo.off()
        else:
            brillo_rojo = min(abs(diferencia) / 5.0, 1.0)
            led_rojo.value = brillo_rojo
            led_azul.off()

        print(f"Temp. Potenciometro: {temperatura_pot:.2f}°C, Temp. Real: {temperatura_real:.2f}°C")

        time.sleep(1)

if __name__ == "__main__":
    try:
        control_proporcional()
    except KeyboardInterrupt:
        print("el programa termino.")
        led_rojo.off()
        led_azul.off()
