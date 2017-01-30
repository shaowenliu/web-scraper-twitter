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
