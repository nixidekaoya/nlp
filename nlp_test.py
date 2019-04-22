# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 22:32:15 2019

@author: LI Mofei
"""

import urllib.request
import chardet
import unicodedata
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = "https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC"
    
    text1 = "はは  ごnini　　ingＣけんＧ"
    
    text2 = unicodedata.normalize('NFKC',text1)
    print('Before:',text1)
    print('After:',text2)
    
    with urllib.request.urlopen(url) as res:
        byte = res.read()
        #decode_dict = chardet.detect(byte)
        #print(decode_dict)
        html = byte.decode('utf-8')
        soup = BeautifulSoup(html,'html.parser')
        title = soup.head.title.text
        #print('[title]:',title)
        
        #for block in soup.find_all(['p','h1','h2','h3','h4','h5']):
            #print('[block]:',block.text)
        #print(html)