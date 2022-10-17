#!/usr/bin/python3
"""
python script that uses REST API, for a given
employee ID about his/her TODO list progress
"""

from json import load
import requests
from sys import argv

if __name__ == "__main__":

def make_request(resource, param=None):
"""Retrieve user from API"""
url = 'https://jsonplaceholder.typicode.com/'
url += resource
