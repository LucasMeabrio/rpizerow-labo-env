from gpiozero import LED, Button
from signal import pause

led_pin = LED(19)  # Cambié el nombre de la variable
button_pin = Button(18)  # Cambié el nombre de la variable

button.when_pressed = led.on # Usé las nuevas variables
button.when_released = led.off  # Usé las nuevas variables

pause()
