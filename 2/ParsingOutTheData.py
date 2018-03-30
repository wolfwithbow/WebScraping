#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: @bowchung
- backslash is escape charater, reads double quotation mark as a character
- 
"""

import requests

url = "http://finance.yahoo.com/quote/AAPL?p=AAPL"

response = requests.get(url)
Indicators = ["Previous Close",
            "Open",
            "Bid",
            "Ask",
            "Day's Range",
            "52 Week Range",
            "Volume",
            "Avg. Volume",
            "Market Cap",
            "Beta",
            "PE Ratio (TTM)",
            "EPS (TTM)",
            "Earnings Date",
            "Dividend & Yield",
            "Ex-Dividend Date",
            "1y Target Est"]
print(response)
print(response.status_code)

htmlText = response.text
# print all text
print(response.text)

splitList = htmlText.split("Day's Range")
#take the second element of our splitlist
#print("Search To Find", splitList[1].split(" -->")[1])

# input results to variable
afterFirstSplit = splitList[1].split(" -->")[1]
# check output
# print(afterFirstSplit)
#try to split again
#print("Search To Find", afterFirstSplit.split("<!--")[0])
afterSecondSplit = afterFirstSplit.split("<!--")[0]
#save in data variable - first element
data = afterSecondSplit
print(data)


#stringExample = "AGbCbDbE"
#print(stringExample.split("b"))

