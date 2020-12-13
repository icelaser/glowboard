import time
import RPi.GPIO as GPIO
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI

# Bitte hier die Anzahl der Pixel angeben die unter deinem
# Longboard verbaut wurden. Bei mir z.B. 56 Pixel
# ----------------------------------------------------
PIXEL_COUNT = 56
# ----------------------------------------------------

# definition des Pixel
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, spi=SPI.SpiDev(0, 0), gpio=GPIO)

# Hier sind Methoden definiert, die unten im Main benutzt werden

# Methode: initialisiert die LED's mit allen Möglichen Farben (Regenbogen)
def rainbow_start(pixels, wait=0.1):
    for i in range(pixels.count()):
        pixels.set_pixel(i, wheel(((i * 256 // pixels.count())) % 256) )
        pixels.show()
        if wait > 0:
            time.sleep(wait)

# Methode: Regenbogen Farben im Kreis laufen lassen
def rainbow_run(pixels, wait=0.005):
    for j in range(256):
        for i in range(pixels.count()):
            pixels.set_pixel(i, wheel(((i * 256 // pixels.count()) + j) % 256) )
        pixels.show()
        if wait > 0:
            time.sleep(wait)

# Methode: Pixel langsam ausmachen
def go_off(pixels, wait=0.01, step=1):
    for j in range(int(256 // step)):
        for i in range(pixels.count()):
            r, g, b = pixels.get_pixel_rgb(i)
            r = int(max(0, r - step))
            g = int(max(0, g - step))
            b = int(max(0, b - step))
            pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color( r, g, b ))
        pixels.show()
        if wait > 0:
            time.sleep(wait)

# Methode: Farben wechsel (alle Pixel leuchten in den gleichen Farben)
def color_cycle(pixels, wait=0.05):
    for j in range(256):
        for i in range(pixels.count()):
            pixels.set_pixel(i, wheel(((256 // pixels.count() + j)) % 256) )
        pixels.show()
        if wait > 0:
            time.sleep(wait)

# Main Mehotde: In welcher Reihenfolge die Methoden ausgeführt werden sollen
if __name__ == "__main__":
    while True:
        pixels.clear()
        pixels.show()
        rainbow_start(pixels, wait=0.1)
        rainbow_run(pixels, wait=0.01)
        rainbow_run(pixels, wait=0.01)
        rainbow_run(pixels, wait=0.01)
        go_off(pixels)
        color_cycle(pixels)
        go_off(pixels)
