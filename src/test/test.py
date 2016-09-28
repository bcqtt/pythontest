'''
Created on 2016年9月28日

@author: gionee
'''
import feedparser
ny=feedparser.parse('http://newyork.craigslist.org/stp/index.rss')
print(ny)