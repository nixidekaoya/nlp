# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 22:32:29 2019

@author: LI Mofei
"""

import re
import unicodedata
from bs4 import BeautifulSoup


# Text Normalization
def cleanse(text):
    text = unicodedata.normalize('NFKC',text)
    text = re.sub(r'\s+',' ',text)
    return text


def scrape(html):
    soup = BeautifulSoup(html, 'html.parser')
    #insert <__EOS__>
    for block in soup.find_all(['br','p','h1','h2','h3','h4']):
        if len(block.text.strip()) > 0 and block.text.strip()[-1] not in ['。','！','.','!']:
            block.append('<__EOS__>')
    
    #extract text
    text = '\n'.join([cleanse(block.text.strip()) for block in soup.find_all(['p','h1','h2','h3','h4','h5']) if len(block.text.strip()) > 0])
    #title text
    title = cleanse(soup.title.text.replace(' - Wikipedia',''))
    return text,title