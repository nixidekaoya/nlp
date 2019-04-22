# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 19:06:09 2019

@author: LI Mofei
"""

import urllib.request
#import chardet
import scrape

if __name__ == '__main__':
    url = "https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC"
    with urllib.request.urlopen(url) as res:
        byte = res.read()
        html = byte.decode('utf-8')
        text, title = scrape.scrape(html)
        print('[title]:',title)
        print('[text]:',text)