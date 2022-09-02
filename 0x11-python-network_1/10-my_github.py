#!/usr/bin/python3
"""
Python script
"""


import requests
from sys import argv

if __name__ == "__main__":
    """
    Script that takes your GitHub credentials (username and
    password) and uses the GitHub API to display your id
    """

    url = 'https://api.github.com/user'

    req = requests.get(url, auth=(argv[1], argv[2])).json()

    print(req.get("id"))
