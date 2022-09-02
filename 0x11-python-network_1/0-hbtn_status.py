#!/usr/bin/python3
"""
Python script non-importable
"""


import urllib.request

if __name__ == "__main__":
    """
    Python script that fetches https://intranet.hbtn.io/status
    saving the request in a var and opening using urlopen func
    """
    req = urllib.request.Request("https://intranet.hbtn.io/status")

    with urllib.request.urlopen(req) as res:
        html = res.read()
        print("Body response:")
        print(f"\t- type: {type(html)}")
        print(f"\t- content: {html}")
        print(f"\t- utf8 content: {html.decode('utf-8')}")
