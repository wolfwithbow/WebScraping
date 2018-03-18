#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: bow
copy list
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
#get html code
#print(response.text)

#response.text will hold the html text
htmlText = response.text

#play, find good way to get data
#call split method - takes a text
#and splits at that value
splitList = htmlText.split("Bid")
afterFirstSplit = splitList[1].split(" -->")[1]
#3 elements
#element with index 1 (second element)

afterSecondSplit = afterFirstSplit.split("<!-- ")
#save in data variable
data = afterSecondSplit[0]
print(data)

#example split
#stringExample = "AGbCbDbE"
#print(stringExample.split("b"))


#Parse list




