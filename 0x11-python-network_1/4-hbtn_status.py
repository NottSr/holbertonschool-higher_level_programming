#!/usr/bin/python3
"""
Python script
"""


import requests

if __name__ == "__main__":
    """
    Script that fetches https://intranet.hbtn.io/status
    """
    html = requests.get("https://intranet.hbtn.io/status")
    print("Body response:\n\t- type: {}\n\t- content: {}".format(
        type(html.text),
        html.text
        ))
