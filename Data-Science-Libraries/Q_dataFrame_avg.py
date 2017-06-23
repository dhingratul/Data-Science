#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 11:30:25 2017

@author: dhingratul
"""

from pandas import DataFrame, Series
import numpy as np


def avg_medal_count():
    '''
    Compute the average number of bronze medals earned by countries who
    earned at least one gold medal.
    Save this to a variable named avg_bronze_at_least_one_gold. You do not
    need to call the function in your code when running it in the browser -
    the grader will do that automatically when you submit or test it.
    '''

    countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                 'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                 'Austria', 'France', 'Poland', 'China', 'Korea',
                 'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

    gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1,
            1, 0, 0, 0, 0, 0]
    silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0,
              0, 2, 2, 2, 1, 0]
    bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1,
              0, 6, 2, 1, 0, 1]

    olympic_medal_counts = {'country_name': Series(countries),
                            'gold': Series(gold),
                            'silver': Series(silver),
                            'bronze': Series(bronze)}
    df = DataFrame(olympic_medal_counts)
    oneGold = df['gold'] >= 1
    df_oneGold = df[oneGold]
    avg_bronze_at_least_one_gold = np.mean(df_oneGold['bronze'])
    return avg_bronze_at_least_one_gold
