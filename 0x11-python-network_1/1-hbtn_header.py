#!/usr/bin/python3
"""
Python script
"""

from sys import argv
from urllib import request

if __name__ == "__main__":
    """
    Script that takes in a URL, sends a request to
    the URL and displays the value of the X-Request-Id
    variable found in the header of the response.
    """
    url = argv[1]

    req = request.Request(url)

    with request.urlopen(req) as res:
        print(res.headers.get('X-Request-Id'))
