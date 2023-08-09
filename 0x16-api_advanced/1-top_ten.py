#!/usr/bin/python3
"""
   a function that queries the Reddit API and returns the number of subscribers
"""


import requests


def top_ten(subreddit):
    '''
    to fetchthe top ten posts
    '''
    headers_dict = {'User-Agent':
                    "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    url = "https://www.reddit.com/r/{}/top.json".format(subreddit)
    someParams = {'limit': '10'}
    res = requests.get(url, params=someParams,
                       allow_redirects=False, headers=headers_dict)
    if res.status_code == 200:
        result = res.json()
        data = result.get("data").get("children")
        for title in data:
            print(title.get('data').get('title'))
    else:
        print("None")
