#!/usr/bin/python3
"""
Python script
"""


from urllib import request

if __name__ == "__main__":
    """
    Python script that fetches https://intranet.hbtn.io/status
    """
    req = request.Request("https://intranet.hbtn.io/status")

    with request.urlopen(req) as res:
        html = res.read()

    print(f"Body response:\n\
    - type: {type(html)}\n\
    - content: {html}\n\
    - utf8 content: {html.decode('UTF8')}")
