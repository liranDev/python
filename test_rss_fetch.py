import unittest
from rss import RSSFetcher
from dbapi import DBAPI

URL = 'http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'



class TestRssFetcher(unittest.TestCase):
     
        
        
 
    def test_fetch_data(self):

        rssFetcher = RSSFetcher()
        db = DBAPI()

        db.connect_to_db('rssDB')
        db.clean_collection('rss')
        
        rssFetcher.fetch_data(URL)
        
        query = 'self.db.rss.count()'
        result = db.exec_query(query)

        self.assertEqual(1, result)
 
 
        db.close_connection()
    





