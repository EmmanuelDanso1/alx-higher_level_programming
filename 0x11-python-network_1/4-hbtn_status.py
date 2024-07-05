#!/usr/bin/python3
"""
Using request to get url link
"""
import requests

if __name__== "__main__":

    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    body = response.text
    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")

