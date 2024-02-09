#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 11:07:55 2024

@author: alossius
"""

# Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import UnicornPy as UniPy
from neurol import streams
from neurol.connect_device import get_lsl_EEG_inlets
from neurol.BCI import generic_BCI, automl_BCI
from neurol import BCI_tools
from neurol.models import classification_tools
from pylsl import StreamInlet, resolve_stream

'''
GOALS
- Stream live data from two unicorn headsets in parallel
    - start with conencting 1 headset and steaming data
    - try to connect another and also stream
- Process the data live and in parallel
- Plot the data live and in parallel
'''

'''
Refer to https://github.com/merlin-neurotech/Speller-GPT/blob/main/GPTherAI.py for an example
'''

#%% Step 1 - Connect to the UNICORN headset
<<<<<<< HEAD
=======

>>>>>>> c00bd0d0feab1281f9af05dc34ae030cfe524e5c
