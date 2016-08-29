import os
import bs4
from selenium import webdriver
import urllib2
from bs4 import BeautifulSoup

"""
download bs4 by using pip install bs4 on the command line
download selenium by using pip install selenium on the command line
"""

"""
This is a damn crude code i just wrote, but it sure downloads something

"""
class Downloader:
    
    def __init__(self, url, title):
        self.url = url
        self.title = title
        
    def openPage(self):
        newpage = urllib2.urlopen(self.url).read()
        return newpage
    
    def getTitle(self):
        firstletter = self.title[0].lower()
        print firstletter
        return firstletter
    
    def getSeriesPage(self):
        page = self.openPage()
        firsttitle = ''
        if self.getTitle() in "a,b,c".split(','):
            firsttitle = 'a'
        elif self.getTitle() in "d,e,f".split(','):
            firsttitle = 'd'
        elif self.getTitle() in "g,h,i".split(','):
            firsttitle = 'g'
        elif self.getTitle() in "j,k,l".split(','):
            firsttitle = 'j'
        elif self.getTitle() in "m,n,o".split(','):
            firsttitle = 'm'
        elif self.getTitle() in "p,q,r".split(','):
            firsttitle = 'p'
        elif self.getTitle() in "s,t,u".split(','):
            firsttitle = 's'
        elif self.getTitle() in "v,w,x".split(','):
            firsttitle = 'v'
        elif self.getTitle() in "y,z,0,1,2,3,4,5,6,7,8,9,#".split(','):
            firsttitle = 'y'
        #print firsttitle
        return firsttitle
    
    def openSeriesPage(self):
        seriesPage = "{}/{}".format(self.url, self.getSeriesPage())
        newpage = urllib2.urlopen(seriesPage).read()
        newsoup = BeautifulSoup(newpage, 'html.parser')
        
        links = newsoup.find_all('a')
        
        for tags in links:
            link = tags.get('href', None)
            if link is not None:
                pass
        return seriesPage
    
    def downloadSeries(self):
        browser = webdriver.Firefox()
        browser.get(self.openSeriesPage())
        
        serieslink = browser.find_element_by_link_text("Game of Thrones")
        serieslink.click()
        
        selectSeason = browser.find_element_by_link_text("Season 06")
        selectSeason.click()
        
        selectEpisode = browser.find_element_by_link_text("Episode 01")
        selectEpisode.click()
        
        selectVideo = browser.find_element_by_link_text("Game of Thrones - S06E01 (TvShows4Mobile.Com).mp4")
        selectVideo.click()
        
        
         

url = "http://o2tvseries.com"
title = "Game of Thrones"

newDownloader = Downloader(url, title)
#newDownloader.getTitle()
newDownloader.openSeriesPage()
newDownloader.downloadSeries()
