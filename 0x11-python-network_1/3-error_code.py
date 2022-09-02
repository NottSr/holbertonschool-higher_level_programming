#!/usr/bin/python3
"""
Python script
"""


from sys import argv
from urllib import request, error

if __name__ == "__main__":
    """
    script that takes in a URL, sends a request to
    the URL and displays the body of the response.
    """

    url = argv[1]

    try:
        with request.urlopen(url) as res:
            html = res.read()
            print(html.decode('utf-8'))
    except error.URLError as err:
        print(f"Error code: {err}")
