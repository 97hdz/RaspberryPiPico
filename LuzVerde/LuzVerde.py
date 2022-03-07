from machine import Pin, Timer

led = Pin(25, Pin.OUT)
LED_state = True
t = Timer()

def luzDeMierda(t):
    global led, LED_state
    LED_state = not LED_state
    led.value(LED_state)
    
t.init(freq=1, mode=Timer.PERIODIC, callback=luzDeMierda)