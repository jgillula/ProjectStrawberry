#!/usr/bin/env python

import twitter, pickle
from datetime import datetime

class TwitterChangeTracker:
    def __init__(self, user, credentials_filename):
        self.user = user

        self.lastChangeTimestamp = None
        credentials_file = open(credentials_filename)
        credentials = pickle.load(credentials_file)
        credentials_file.close()
        self.api = twitter.Api(access_token_key=credentials["access_token_key"],
                               access_token_secret=credentials["access_token_secret"],
                               consumer_key=credentials["consumer_key"],
                               consumer_secret=credentials["consumer_secret"])
        
            
    def __str__(self):
        if self.lastChangeTimestamp:
            return "Twitter user " + self.user + " last changed at " + str(self.lastChangeTimestamp)
        else:
            return "Twitter user " + self.user + " hasn't been checked yet"

    
    def changed(self):
        statuses = self.api.GetUserTimeline(screen_name=self.user)
        if statuses:
            lastChangeTimestamp = datetime.fromtimestamp(max([status.created_at_in_seconds for status in statuses]))
            if self.lastChangeTimestamp == None:
                self.lastChangeTimestamp = lastChangeTimestamp
                return False            
            elif lastChangeTimestamp > self.lastChangeTimestamp:
                self.lastChangeTimestamp = lastChangeTimestamp
                return True
            else:
                return False

        return None
