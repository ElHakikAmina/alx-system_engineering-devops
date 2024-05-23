#!/usr/bin/python3
""" Query the Reddit API and prints the titles of the first 10 hot posts """

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """ Return top 10 hot posts titles """
    api_url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {
        "user-agent": "windows:0x16.api.advanced:v1.0.0 (by /u/mira)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100,
    }
    response = requests.get(api_url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code != 200:
        return None

    data = response.json().get('data')
    after += data.get('after')
    connt += data.get('dist')
    for post in data.get('children'):
        hot_list.append(post.get('data').get('title'))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    return hot_list
