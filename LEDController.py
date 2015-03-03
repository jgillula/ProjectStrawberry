#!/usr/bin/env python

import RPi.GPIO as GPIO

class LEDController:
    def __init__(self, rgbChannels, frequency=50)
        self.rgbChannels = rgbChannels

        GPIO.setmode(GPIO.BOARD)
        for pin in self.rgbChannels:
            GPIO.setup(pin, GPIO.OUT)

        self.rgbPWMs = []
        for pin in self.rgbChannels:
            self.rgbPWMs.append(GPIO.PWM(pin, frequency))

                
    def setRGB(self, rgbVal):
        self.stop()
        for pwm, value in zip(self.rgbPWMs, rgbVal):
            value = max(min(value, 100.0), 0.0)
            pwm.start(value)


    def stop(self):
        for pwm in self.rgbPWMs:
            pwm.stop()


    def __del__(self):
        self.stop()
        GPIO.cleanup()
