#!/usr/bin/env python

import feedparser
from datetime import datetime

class RSSChangeTracker:
    def __init__(self, URL):
        self.URL = URL

        self.lastChangeTimestamp = datetime.utcnow()
            
            
    def __str__(self):
        if self.lastChangeTimestamp:
            return "RSS feed " + self.URL + " last changed at " + str(self.lastChangeTimestamp)
        else:
            return "RSS feed " + self.URL + " hasn't been checked yet"

    
    def changed(self):
        feed = feedparser.parse(self.URL)
        if feed:
            if feed.has_key('updated_parsed'):
                lastChangeTimestamp = datetime(feed['updated_parsed'].tm_year, 
                                               feed['updated_parsed'].tm_mon,
                                               feed['updated_parsed'].tm_mday,
                                               feed['updated_parsed'].tm_hour,
                                               feed['updated_parsed'].tm_min,
                                               feed['updated_parsed'].tm_sec)
                if lastChangeTimestamp > self.lastChangeTimestamp:
                    self.lastChangeTimestamp = lastChangeTimestamp
                    return True
                else:
                    return False

        return None
