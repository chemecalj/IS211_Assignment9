#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS_211 Week 9, Assignment 2 Apple Stock"""

import urllib2
import json
from bs4 import BeautifulSoup

url = 'http://finance.yahoo.com/quote/AAPL/history?ltr=1'
stockpage = urllib2.urlopen(url)
soupparse = BeautifulSoup(stockpage.read(), "lxml")

def applestock():
    rows = soupparse.find_all('tr')
    for i in rows:
        try:
            date = i.contents[0].get_text()
            close = i.contents[5].get_text()
            json_string = {"Date": date, "Closing Price": close}
            print(json.dumps(json_string))
        except:
            continue
    return

if __name__ == "__main__":
    applestock()
