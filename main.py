#!/usr/bin/env python

from datetime import datetime
from time import sleep
import syslog, inspect

from RSSChangeTracker import RSSChangeTracker
from TwitterChangeTracker import TwitterChangeTracker
from LEDController import LEDController


syslog.openlog(logoption=syslog.LOG_PID, facility=syslog.LOG_LOCAL0)

def log(changeTracker):
    syslog.syslog("Project-Strawberry:[{}] ".format(inspect.currentframe().f_back.f_lineno) + str(changeTracker))

if __name__ == "__main__":
    ledController = LEDController()
    
    ledController.rainbowCycle(wait_ms=1, iterations=8)
    ledController.colorWipe(0,0,0)

    deeplinks = RSSChangeTracker("https://www.eff.org/rss/updates.xml")
    twitter = TwitterChangeTracker("eff", "/home/pi/ProjectStrawberry/credentials.pickle")
    shariSignal = RSSChangeTracker("https://www.eff.org/5PBmKovAHhFoqP91B6ngMNosLIDY96cp.xml")

    log('Online!')

    while True:
        if deeplinks.changed():
            log(deeplinks)
            ledController.pulseAll(255,0,0,wait_ms=0.01,iterations=6)
            ledController.waveChase(255,0,0,length=8,iterations=3)
            ledController.waveChase(255,0,0,length=8,iterations=3,fade=True)

        if twitter.changed():
            log(twitter)
            for iteration in range(5):
                ledController.colorWipe(0,128,255,30)
                ledController.colorWipe(0,0,0,30)
        
        if shariSignal.changed():
            log(shariSignal)
            ledController.theaterChaseRainbow(wait_ms=20,iterations=1)
            ledController.rainbow(wait_ms=30,iterations=5)
            ledController.rainbow(wait_ms=30,iterations=2, fade=True)

        sleep(60)
