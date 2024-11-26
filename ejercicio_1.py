from gpiozero import LED, Button
from signal import pause

led_pin = LED(19) 
button_pin = Button(18)

button.when_pressed = led.on 
button.when_released = led.off  

pause()
