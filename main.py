#!/usr/bin/env python

from datetime import datetime
from time import sleep

from RSSChangeTracker import RSSChangeTracker
from TwitterChangeTracker import TwitterChangeTracker


if __name__ == "__main__":
    changeTrackers = []
    changeTrackers.append(RSSChangeTracker("https://www.eff.org/rss/updates.xml"))
    changeTrackers.append(TwitterChangeTracker("eff", "credentials.pickle"))

    while True:
        for changeTracker in changeTrackers:
            if changeTracker.changed():
                print str(datetime.utcnow()) + ": " + str(changeTracker)
        
        sleep(60)
