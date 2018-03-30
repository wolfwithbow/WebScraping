#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: maxschallwig
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

#get the html code - call the text element
#print(response.text)
#give it a variable called htmlText
htmlText = response.text

#we want to split by the previous close manually
#print(htmlText.split("Previous Close"))

#example showing how split works
#everytime 'b' occurs its going to create a new element in the list
#stringExample = "ABSFDFenf"
#print(stringExample.split("S"))

#
splitList = htmlText.split("Previous Close")
#length of split list - 3 multiple occurences
print(len(splitList))

#stringExample = "AGbCbDbE"
#print(stringExample.split("b"))


