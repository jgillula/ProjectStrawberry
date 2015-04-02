#!/usr/bin/env python

import feedparser, random, string

class RSSChangeTracker:
    def __init__(self, URL):
        self.URL = URL

        self.lastChangeTimestamp = None
        self.latestTitle = ""        

            
    def __str__(self):
        if self.lastChangeTimestamp:
            return "RSS feed " + self.URL + " last changed at " + str(self.lastChangeTimestamp) + " with title " + self.latestTitle
        else:
            return "RSS feed " + self.URL + " hasn't been checked yet"

    
    def changed(self):
        feed = feedparser.parse(self.URL+'?'+''.join([random.choice(string.ascii_letters) for n in xrange(32)]))
        if feed:
            if feed.has_key('updated_parsed'):
                lastChangeTimestamp = feed['updated_parsed']
                latestTitle = sorted([(entry.published_parsed, entry.title) for entry in feed.entries], reverse=True)[0][1]
                if self.lastChangeTimestamp is None:
                    self.lastChangeTimestamp = feed['updated_parsed']
                    self.latestTitle = latestTitle
                    return None
                elif lastChangeTimestamp > self.lastChangeTimestamp and self.latestTitle != latestTitle:
                    self.lastChangeTimestamp = lastChangeTimestamp
                    self.latestTitle = latestTitle
                    return True
                else:
                    return False

        return None
