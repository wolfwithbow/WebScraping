#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: maxschallwig
"""
#import requests library
import requests

url = "http://finance.yahoo.com/quote/AAPL?p=AAPL"

#access request library
#send a get request by calling the get method
#save in variable called response
#returns html code
response = requests.get(url)


print(response)
print(response.status_code)

#check wikipedia for status code