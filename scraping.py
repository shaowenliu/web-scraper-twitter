#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 13:31:08 2017

@author: Shaowen Liu
"""

import sys, getopt
from bs4 import BeautifulSoup

import toolkits
def main(argv):
    user_name = ''
    num = 5
    try:
        opts, args = getopt.getopt(argv,'u:n:', ['user=', 'number='])
    except getopt.GetoptError:
        print('scraping.py -u <user> -n <number>')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-u','--user'):
            user_name = arg
        elif opt in ('-n', '--number'):
            num = int(arg)
    if not user_name:
        print('''please input a user name. e.g.
$ python scraping.py -u realDonaldTrump''')
        sys.exit()
            
    url = 'https://twitter.com/{}'.format(user_name)
    html = toolkits.get_html(url)
    
    try:  
        # html is found
        soup = BeautifulSoup(html.read(), 'lxml')
        tweets = soup.find_all('div', {'class': 'content'})
    except AttributeError:
        print('html or tag is not found.')
        
    for tweet in tweets[:num]:
        t_time = tweet.find('a', {'class': 'tweet-timestamp js-permalink js-nav js-tooltip'})
        t_text = tweet.find('div', {'class': 'js-tweet-text-container'})
        content = t_text.get_text()
        counts = tweet.find_all('span', {'class': 'ProfileTweet-actionCountForPresentation'})
        reply = counts[0].get_text()
        retweet = counts[1].get_text()
        like = counts[3].get_text()
        # print out
        print(t_time.attrs['title'])
        print('Contents: {}'.format(content.rstrip('\n')))
        print('Reply: {}'.format(reply))
        print('Retweet: {}'.format(retweet))
        print('Like: {}\n\n'.format(like))
    
if __name__ == '__main__':
    main(sys.argv[1:])
    
    
    
    
    
    
    
    
    
    