#!/usr/bin/python3
"""
script that queries Reddit API and returns
number of subscribers for a given subreddit.
if invalid, return 0
"""
import json
import requests
import sys

headers = {'User-Agent': 'My User Agent 1.0'}


def number_of_subscribers(subreddit):
	"""
	function that returns the number
	of subscribers
	"""
	try:
		url = 'https://www.reddit.com/r/'
		response = requests.get(url + subreddit + "/about.json",
					headers=headers, allow_redirects=False)
		return response.json()['data']['subscribers']
	except:
		return 0
