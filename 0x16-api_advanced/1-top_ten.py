#!/usr/bin/python3
""" Query the Reddit API and prints the titles of the first 10 hot posts """

import requests


def top_ten(subreddit):
    """ Return top 10 hot posts titles """
    api_url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {
        "user-agent": "windows:0x16.api.advanced:v1.0.0 (by /u/mira)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(api_url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code != 200 or not response.text:
        print('None')
        return

    data = response.json().get('data')
    for post in data.get('children'):
        print(post.get('data').get('title'))
