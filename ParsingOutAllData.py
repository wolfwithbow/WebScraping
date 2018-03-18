#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: bow
copy list
"""

import requests

url = "http://finance.yahoo.com/quote/AAPL?p=AAPL"
#new dictionary called data
data = {}
response = requests.get(url)
Indicators = {"Previous Close":[],
            "Open":[],
            "Bid":[],
            "Ask":[],
            "DAYS_RANGE-value":[],
            "52 Week Range":[],
            "Volume":[],
            "Avg. Volume":[],
            "Market Cap":[],
            "Beta":[],
            "PE Ratio (TTM)":[],
            "EPS (TTM)":[],
            "Earnings Date":[],
            "Dividend &amp; Yield":[],
            "Ex-Dividend Date":[],
            "1y Target Est":[]}
print(response)
print(response.status_code)

htmlText = response.text
#exception add print
#print(htmlText)
for indicator in Indicators:
    #exceptin add break
    #break
    print(indicator)
    splitList = htmlText.split(indicator)
    afterFirstSplit = splitList[1].split(" -->")[1]
    afterSecondSplit = afterFirstSplit.split("<!-- ")
    dataValue = afterSecondSplit[0]
    #look at corresponding key and append the data (change to dataValue so we dont have conflicting names)
    Indicators[indicator].append(dataValue)
    
print(Indicators)