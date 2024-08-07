#!/usr/bin/python3
"""
Python scripts to get the email
"""
import sys
import requests

if __name__=="__main__":
    """
    Binding sys to argv
    """
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email':email}
    response = requests.post(url, data=data)
    print(response.text)

