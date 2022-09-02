#!/usr/bin/python3
"""
Python script
"""


import requests
from sys import argv

if __name__ == "__main__":
    """
    Script that takes in a URL, sends a request to the URL
    and displays the body of the response.
    """

    url = argv[1]

    html = requests.get(argv[1])
    if html.status_code >= 400:
        print("Error code:", html.status_code)
    else:
        print(html.text)
