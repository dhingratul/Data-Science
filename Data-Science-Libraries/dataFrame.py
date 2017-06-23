#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 11:49:04 2017

@author: dhingratul
"""
import pandas as pd
d = {'name': pd.Series(['AD', "BD", "CD", "DE"], index=[1, 2, 3, 4]),
     'age': pd.Series([12, 32, 44], index=[1, 3, 4])}
df = pd.DataFrame(d)
print(df)
