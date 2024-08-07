#!/usr/bin/python3
"""
Script which emphasizes on JSON and API
"""
import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) < 2 else sys.argv[1]

    data = {"q": letter}
    req = requests.post("http://0.0.0.0:5000/search_user", data=data)

    try:
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
