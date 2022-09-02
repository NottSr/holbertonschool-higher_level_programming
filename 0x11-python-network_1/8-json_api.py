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
        q = argv[2]

    try:
        url = "http://0.0.0.0:5000/search_user"
        value = {'q': q}

        html = requests.post(url, data=value)

        html_j = html.json()
        if {'id', 'name'} <= html_j.keys():
            print("[{}] {}".format(html_j.get("id"), html_j.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
