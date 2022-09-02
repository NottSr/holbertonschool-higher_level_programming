#!/usr/bin/python3
"""
Python script non-importable
"""


from sys import argv
import urllib.error
import urllib.request

if __name__ == "__main__":
    """
    script that takes in a URL, sends a request to
    the URL and displays the body of the response.
    """

    url = argv[1]

    try:
        with urllib.request.urlopen(url) as res:
            html = res.read()
            print(html.decode('utf-8'))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
