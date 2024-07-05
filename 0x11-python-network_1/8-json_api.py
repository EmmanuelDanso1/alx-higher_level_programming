#!/usr/bin/python3
"""
Scripting for Json and API
"""
import requests
import sys

if __name__=="__main__":
    url = "http://0.0.0.0:5000/search_user"
    the_letter = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {'q': the_letter}
    response = requests.post(url, data)
    try:
        json_response = response.json()
        if json_response:
            print(f"[{json_response.get('id')}]{json_response.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
