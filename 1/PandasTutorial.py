#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: maxschallwig
"""

#import pandas
import pandas as pd

#3 keys
inputData = {"Data1":[1,2,3,4,5,6],
             "Data2":[5,6,7,8,9,10],
             "Data3":[9,10,11,12,13,14]}
             
#print
#lists are maintained
print(inputData)

#create a data frame
df = pd.DataFrame(inputData)
print()
print(df)
print(df.head(2))
print(df.tail(3))