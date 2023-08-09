#!/usr/bin/python3
"""
   a function that queries the Reddit API and returns the number of subscribers
"""


import requests


def number_of_subscribers(subreddit):
    '''
    to fetch the number of subscribers
    '''
    headers_dict = {'User-Agent':
                    "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, allow_redirects=False, headers=headers_dict)
    if res.status_code == 200:
        data = res.json().get("data")
        return data.get("subscribers")
    else:
        return 0
