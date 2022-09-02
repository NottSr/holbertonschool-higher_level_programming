#!/usr/bin/python3
"""
Python script
"""


from sys import argv
import requests

if __name__ == "__main__":
    """
    Script that takes in a URL, sends a request to the URL
    and displays the value of the variable X-Request-Id in
    the response header
    """
    url = argv[1]

    html = requests.get(url)
    print(html.headers.get('X-Request-Id'))
