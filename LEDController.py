#!/usr/bin/env python

import time, math

from neopixel import *

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

class LEDController:
    def __init__(self, 
                 LED_COUNT      = 15,   
                 LED_PIN        = 18,
                 LED_FREQ_HZ    = 800000,
                 LED_DMA        = 5,
                 LED_BRIGHTNESS = 255,
                 LED_INVERT     = False):
        self.strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
        # Intialize the library (must be called once before other functions).
        self.strip.begin()
        

    def blank(self):
        self.setAll(0,0,0)

    def setAll(self, red, green, blue):
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, Color(int(green), int(red), int(blue)))
        self.strip.show()


    def pulseAll(self, red, green, blue, wait_ms=5, iterations=1):
        for iteration in range(iterations):
            for percent in range(100)+range(100,-1,-1):
                self.setAll(red*percent/100.0, green*percent/100.0, blue*percent/100.0)
                time.sleep(wait_ms/1000.0)
                


    def colorWipe(self, red, green, blue, wait_ms=50):
	"""Wipe color across display a pixel at a time."""
	for i in range(self.strip.numPixels()):
		self.strip.setPixelColor(i, Color(green,red,blue))
		self.strip.show()
		time.sleep(wait_ms/1000.0)


    def rainbow(self, wait_ms=5, iterations=1,fade=False):
	"""Draw rainbow that fades across all pixels at once."""
        brightness = float(255)

	for j in range(256*iterations):
		for i in range(self.strip.numPixels()):
			self.strip.setPixelColor(i, wheel((i+j) & 255))
                if fade:
                    self.strip.setBrightness(int(brightness))
                    brightness = max(0.0, float(brightness) - 255.0/float(256.0*iterations-1))
		self.strip.show()
		time.sleep(wait_ms/1000.0)

        if fade:
            self.__cleanupFade__()




    def rainbowCycle(self, wait_ms=20, iterations=1, fade=False):
	"""Draw rainbow that uniformly distributes itself across all pixels."""
        brightness = float(255)

	for j in range(256*iterations):
		for i in range(self.strip.numPixels()):
			self.strip.setPixelColor(i, wheel(((i * 256 / self.strip.numPixels()) + j) & 255))
                if fade:
                    self.strip.setBrightness(int(brightness))
                    brightness = max(0.0, float(brightness) - 255.0/float(256.0*iterations-1))
		self.strip.show()
		time.sleep(wait_ms/1000.0)
        if fade:
            self.__cleanupFade__()


    def theaterChaseRainbow(self, wait_ms=50,iterations=1):
	"""Rainbow movie theater light style chaser animation."""
        for iteration in range(iterations):

            for j in range(256):
		for q in range(3):
                    for i in range(0, self.strip.numPixels(), 3):
                        self.strip.setPixelColor(i+q, wheel((i+j) % 255))
                    self.strip.show()
                    time.sleep(wait_ms/1000.0)
                    for i in range(0, self.strip.numPixels(), 3):
                        self.strip.setPixelColor(i+q, 0)

    def leadChase(self, red, green, blue, wait_ms=50, iterations=1, length=None, fade=False):
        if length == None:
            length = self.strip.numPixels()

        brightness = float(255)

        for iteration in range(iterations):
            for start_index in range(self.strip.numPixels()):                
                end_index = start_index + length
                for i in range(start_index, end_index):
                    percent = float(i-start_index)/length
                    
                    self.strip.setPixelColor(i % self.strip.numPixels(), Color(int(green*percent), int(red*percent), int(blue*percent)))
                if fade:
                    self.strip.setBrightness(int(brightness))
                    brightness = max(0.0, float(brightness) - 255.0/float(iterations*self.strip.numPixels()-1))
                self.strip.show()
                time.sleep(wait_ms/1000.0)
        if fade:
            self.__cleanupFade__()


    def waveChase(self, red, green, blue, wait_ms=50, iterations=1, length=None, fade=False):
        if length == None:
            length = self.strip.numPixels()

        brightness = float(255)

        for iteration in range(iterations):
            for start_index in range(self.strip.numPixels()):                
                end_index = start_index + length
                for i in range(start_index, end_index):
                    percent = (1.0+math.cos(math.pi*2.0*float(i-start_index)/length + math.pi))/2.0
                    self.strip.setPixelColor(i % self.strip.numPixels(), Color(max(0,int(green*percent)), max(0,int(red*percent)), max(0,int(blue*percent))))
                if fade:
                    self.strip.setBrightness(int(brightness))
                    brightness = max(0.0, float(brightness) - 255.0/float(iterations*self.strip.numPixels()-1))
                self.strip.show()
                time.sleep(wait_ms/1000.0)
        
        if fade:
            self.__cleanupFade__()


    def __cleanupFade__(self):
        self.blank()
        self.strip.setBrightness(255)
