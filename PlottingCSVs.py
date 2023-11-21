# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 09:45:46 2023

@author: General Use
"""

import pandas as pd
import re
import matplotlib.pyplot as plt

name1 = 'UnicornRecorder_20231117_141911.csv'
name2 = 'UnicornRecorder_20231117_141913.csv'

df1 = pd.read_csv(name1)
df2 = pd.read_csv(name2)

match1 = re.search(r'(\d{6})\.csv$', name1)
match2 = re.search(r'(\d{6})\.csv$', name2)

if match1:
    starttime_1 = int(match1.group(1))
    print('Start time 1 found: ' + str(starttime_1))
else:
    print('Start time 1 not found!')
    
if match2:
    starttime_2 = int(match2.group(1))
    print('Start time 2 found: ' + str(starttime_2))
else:
    print('Start time 2 not found!')
    
time_offset = abs(starttime_1 - starttime_2) / 0.004 # counts

count1 = df1['Counter']
count2 = df2['Counter']

if starttime_1 < starttime_2:
    count1 = count1 + time_offset
else:
    count2 = count2 + time_offset

plt.figure(dpi=300)
EEG1_1 = df1['EEG 1'][time_offset:]
#count1 = df1['Counter'][25:100] * 0.004
EEG1_2 = df2['EEG 1']
#count2 = df2['Counter'][25:100] * 0.004

plt.plot(count1, EEG1_1, label='Dataset 1')
plt.plot(count2, EEG1_2, label='Dataset 2')

plt.legend()
plt.show()
    
