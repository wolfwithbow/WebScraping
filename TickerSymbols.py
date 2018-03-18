#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: bow
Extracting Company Ticker Symbols Part 1
Find the first record in the table and print
"""

import requests

url = "http://finance.yahoo.com/quote/AAPL?p=AAPL"
wikiURL = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
response = requests.get(url)

wikiResponse = requests.get(wikiURL)

data = {"Company":[]}

wikiFirstParse = wikiResponse.text.split("0001555280")[0] #view a portion of the table
wikiDataTable = wikiFirstParse.split("Component Stocks")[3] #define the top of the dataset, narrow down range

print(wikiDataTable.split("href=")[5].split('">')[1].split("</")[0]) #5->9->13
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