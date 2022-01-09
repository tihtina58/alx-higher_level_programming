#!/usr/bin/python3
"""comment."""
import requests
from sys import argv

if __name__ == "__main__":

    user = argv[1]
    passwd = argv[2]
    url = 'https://api.github.com/user'

    response = requests.get(url, auth=(user, passwd))
    dict = response.json()
    print(dict.get('id'))
