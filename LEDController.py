#!/usr/bin/env python

import RPi.GPIO as GPIO

class LEDController:
    def __init__(self, rgbChannels = [36,38,40], frequency=50, rgbMax = [100,20,88]):
        self.rgbChannels = rgbChannels
        self.rgbMax = rgbMax

        GPIO.setmode(GPIO.BOARD)
        for pin in self.rgbChannels:
            GPIO.setup(pin, GPIO.OUT)

        self.rgbPWMs = []
        for pin in self.rgbChannels:
            self.rgbPWMs.append(GPIO.PWM(pin, frequency))

                
    def start(self, rgbVal):
        self.stop()
        for pwm, value, maxValue in zip(self.rgbPWMs, rgbVal, self.rgbMax):
            value = max(min(value/maxValue*100.0, 100.0), 0.0)
            pwm.start(value)


    def stop(self):
        for pwm in self.rgbPWMs:
            pwm.stop()


    def __del__(self):
        self.stop()
        GPIO.cleanup()
