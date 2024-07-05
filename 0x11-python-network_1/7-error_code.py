#!/usr/bin/python3
"""
Error handling and exception
"""
import sys
import requests

if __name__=="__main__":
    url = sys.argv[1]
    response = request.get(url)
    
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)

