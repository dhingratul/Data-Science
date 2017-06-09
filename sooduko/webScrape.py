#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 14:18:46 2017

@author: dhingratul

Scraping one HTML page in Python
"""
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = urlopen("http://bit.ly/1D7wKcH").read()
soup = BeautifulSoup(url, "lxml")
text = soup.body.contents
print(text)
