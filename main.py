#!/usr/bin/env python

from datetime import datetime
from time import sleep

from RSSChangeTracker import RSSChangeTracker
from TwitterChangeTracker import TwitterChangeTracker
from LEDController import LEDController

if __name__ == "__main__":
    ledController = LEDController()
    
    ledController.rainbowCycle(wait_ms=1, iterations=8)
    ledController.colorWipe(0,0,0)

    deeplinks = RSSChangeTracker("https://www.eff.org/rss/updates.xml")
    twitter = TwitterChangeTracker("eff", "credentials.pickle")


    while True:
        if deeplinks.changed():
            print str(datetime.utcnow()) + ": " + str(deeplinks)            
            ledController.pulseAll(255,0,0,wait_ms=0.01,iterations=6)
            ledController.waveChase(255,0,0,length=8,iterations=3)
            ledController.waveChase(255,0,0,length=8,iterations=3,fade=True)

        if twitter.changed():
            print str(datetime.utcnow()) + ": " + str(twitter)
            for iteration in range(5):
                ledController.colorWipe(0,128,255,30)
                ledController.colorWipe(0,0,0,30)
        
            #shari:
            #ledController.theaterChaseRainbow(wait_ms=20,iterations=1); ledController.rainbow(wait_ms=30,iterations=2); ledController.blank() for 60 sec

        sleep(60)
