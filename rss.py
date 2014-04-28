from dbapi import DBAPI
import feedparser
from threading import Thread

URL = 'http://feeds.feedburner.com/typepad/outbrain'


class RSSFetcher(Thread):

    def __init__(self):

        Thread.__init__(self)
##        self.setDaemon(True)
        self.db = DBAPI()
        print('Connecting to DB...')
        self.db.connect_to_db('rssDB')
        
        
    def fetch_data(self, url):

        
         processThread = Thread(target = self.collect_data, args = (url,))
         processThread.start()
         processThread.join()

        
    def collect_data(self, args):
            

        print('RSSFetcher:: start collecting data from: ' + args)
        posts = []

        feed = feedparser.parse(args)
            
            
        for entry in feed['entries']:
                
            post = {}
                
            post['title'] = entry.title
            post['description'] = entry.description
            post['url'] = entry.link
            post['publishing date'] = entry.published

            posts.append(post)

        print('RSSFetcher:: start inserting data to db...')
        self.db.insert('rss', {"rss_url":args, "posts":posts})



