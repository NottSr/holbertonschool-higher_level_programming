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
        q = ""
    else:
        q = argv[2]

    html = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})

    try:
        dato = html.json()
        if dato == {}:
            print("No result")
        else:
            print("[{}] {}".format(dato.get("id"), dato.get("name")))
    except ValueError:
        print("Not a valid JSON")
