#!/usr/bin/python3
"""
Python script
"""


import requests
from sys import argv

if __name__ == "__main__":
    """
    Script that takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter.
    """

    if len(argv) == 1:
        q = ''
    else:
        q = argv[1]

    try:
        url = "http://0.0.0.0:5000/search_user"
        value = {'q': q}

        html = requests.post(url, value).json()

        if len(html) == 0:
            print("No result")
        else:
            print("[{}] {}".format(html.get("id"), html.get("name")))
    except ValueError:
        print("Not a valid JSON")
