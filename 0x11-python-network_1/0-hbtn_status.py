#!/usr/bin/python3
"""
Python script
"""


import urllib.request

if __name__ == "__main__":
    """
    Python script that fetches https://intranet.hbtn.io/status
    """
    req = urllib.request.Request("https://intranet.hbtn.io/status")

    with urllib.request.urlopen(req) as res:
        html = res.read()

    print(f"Body response:")
    print(f"- type: {type(html)}")
    print(f"- content: {html}")
    print(f"- utf8 content: {html.decode('UTF8')}")
