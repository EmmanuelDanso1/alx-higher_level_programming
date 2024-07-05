#!/usr/bin/python3
"""Takes GitHub credentials (username and password)
"""
import sys
import requests


if __name__ == "__main__":
    auth = requests.auth.HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = requests.get("https://api.github.com/user", auth=auth)
    print(response.json().get("id"))
