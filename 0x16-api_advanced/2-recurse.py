#!/usr/bin/python3
"""
   a function that queries the Reddit API and returns the number of subscribers
"""


import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    '''
    to fetch the number of subscribers
    '''    
    headers_dict = {'User-Agent':
                    "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    newParams = {
        'after': after,
        'count': count,
        'limit': 100
    }
    res = requests.get(url, params=newParams, allow_redirects=False, headers=headers_dict)
    if res.status_code == 404:
        return None
    newAfter = res.json().get('data').get('after')
    count += res.json().get('data').get('dist')    
    resData = res.json().get('data').get('children')
    for data in resData:
        hot_list.append(data.get('data').get('title'))
    recurse(subreddit, hot_list=hot_list, after=newAfter, count=count)
    return hot_list
