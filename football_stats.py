#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS_211 Week 9, Assignment 1 Football Statistics"""

import urllib2
import json
from bs4 import BeautifulSoup

url = 'http://www.cbssports.com/nfl/stats/playersort/nfl/year-2017-season-regular-category-touchdowns'
footballpage = urllib2.urlopen(url)
soupparse = BeautifulSoup(footballpage.read(), "lxml")

def footballstats():
    row = soupparse.find_all('tr')
    row_number = 0
    if row_number < 20:
        for i in row:
            try:
                player = i.contents[0].get_text()
                position = i.contents[1].get_text()
                team = i.contents[2].get_text()
                touchdowns = i.contents[6].get_text()
                json_string = {"Player Name": player, "Team": team, "Player Position": position, "Touchdown Total": touchdowns}
                print(json.dumps(json_string))
                row_number += 1
            except:
                continue
    return

if __name__ == "__main__":
    footballstats()
