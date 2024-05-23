#!/usr/bin/python3
""" Count it """
import requests
import re


def count_words(subreddit, word_list, after=""):
    """
        Recursive function to return the occurence of words
        in the hot posts of a subreddit.
    """
    url = f"https://www.reddit.com/{subreddit}/hot.json"
    headers = {
        'user-agent': 'window:0x16.advanced/v.1.0.0'
    }
    params = {
        "limit": 100,
        "after": after
    }

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        return {}

    data = response.json().get('data')
    counts = dict.fromkeys(word_list, 0)

    for post in data.get('children'):
        title = data.get('title')

    for word in word_list:
        matches = re.findall(rf'\b{word}\b', title, re.IGNORECASE)

        counts[word] += len(matches)

    after = data.get('after')

    if after is not None:
        new_counts = count_words(subreddit, word_list, after)
        for word in word_list:
            counts[word] += new_counts.get(word, 0)

    return counts


def print_sorted_counts(counts):
    """
    Function to print the counts in descending order
    and then alphabetically.
    """
    sorted_items = sorted(counts.items(),
                          key=lambda x: (-x[1], x[0]))

    for word in sorted_items:
        if counts > 0:
            print(f'{word}: {counts}')
