#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 13:44:31 2017

@author: Shaowen Liu
"""
from urllib.request import urlopen, HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import re

def get_html(url):
    """
    return html from url, 
    else, return None.
    """
    try:
        # this is used to request the original html file on the server
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        """
        HTTPError, html page is not found on the server
        URLError, server is not found
        """
        print('web page not found {}'.format(url))
        return None
    else:
        return html

if __name__ == '__main__':
    html = get_html('http://www.pythonscraping.com/pages/warandpeace.html') 
    #get elements
    try:  
        # html is found
        soup = BeautifulSoup(html.read(),'lxml')
        spans = soup.find_all('span', {'class': re.compile(r'green')})
    except AttributeError:
        print('html or tag is not found.')
    
    #use elements
    for span in spans:
        print(span.get_text())
    """    
    #get elements from multiple tags, or classes
    headers = soup.find_all({'h1','h2'})
    
    # get children of the elements
    html = urlopen("http://www.pythonscraping.com/pages/page3.html")
    soup = BeautifulSoup(html)
    soup.find("table",{"id":"giftList"}).children
              
    # get next_sibling/next_siblings/previous_sibling/previous_siblings
    soup.find("table",{"id":"giftList"}).tr.next_siblings
    
    # get parent
    soup.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling
    
    # get attributes
    tag = soup.find("img",{"src":"../img/gifts/img1.jpg"})
    tag.attrs
    
    # using lambda to filter tag
    soup.findAll(lambda tag: len(tag.attrs) == 2)
    """
