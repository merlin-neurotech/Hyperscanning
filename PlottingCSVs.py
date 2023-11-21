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
    
time_offset =  int(abs(starttime_1 - starttime_2) / 0.004) # counts

startseconds_1 = int(str(starttime_1)[-2:]) #find what second 1 started at
startseconds_2 = int(str(starttime_2)[-2:]) #find what second 2 started at

 
if starttime_1 < starttime_2:
    #convert counter to seconds, make it realtime w startseconds
    count1 = startseconds_1 + (df1['Counter'][time_offset:] * 0.004)
    count2 = startseconds_2 + (df2['Counter'] * 0.004)
    
    EEG1_1 = df1['EEG 1'][time_offset:]
    EEG1_2 = df2['EEG 1']

else:
    count1 = startseconds_1 + (df1['Counter'] * 0.004)
    count2 = startseconds_2 + (df2['Counter'][time_offset:] * 0.004)
    
    EEG1_1 = df1['EEG 1']
    EEG1_2 = df2['EEG 1'][time_offset:]


plt.figure(dpi=300)

plt.plot(count1, EEG1_1, label='Dataset 1')
plt.plot(count2, EEG1_2, label='Dataset 2')

plt.legend()
plt.show()
    
