#!/usr/bin/python3
"""
Scripts that handles exceptions
"""
import urllib.request
import urllib.error
import sys
if __name__== "__main__":

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as respnse:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")

