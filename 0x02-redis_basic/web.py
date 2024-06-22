#!/usr/bin/env python3
"""
The script implements an expiring web cache and tracker
"""
import functools
from typing import Callable

import redis
import requests


def tracker(method: Callable) -> Callable:
    """
    A decorator that tracks how many times an url is accessed
    and caches the result with an expiration time of 10 seconds
    :param method: The method to decorate
    :return: the output of the decorated method
    """

    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        """
        The wrapper function to cache the result
        :param args: positional arguments
        :param kwargs: keyword arguments
        :return: The result of the decorated method
        """
        cache = redis.Redis()
        url = args[0]
        count_key = f"count:{url}"
        data_key = f"data:{url}"

        cache.incr(count_key, 1)

        if cache.exists(data_key):
            return cache.get(data_key).decode("utf-8")

        result = method(*args, **kwargs)
        cache.setex(data_key, 10, result)

        return result

    return wrapper


@tracker
def get_page(url: str) -> str:
    """
    Get the page from a url
    :param url: The url to get the page from
    :return: the html of the page
    """
    r = requests.get(url)
    return r.text
