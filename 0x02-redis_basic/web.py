#!/usr/bin/env python3
"""
The scripts implements a expiring web cache and tracker
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
        :param args:
        :param kwargs:
        :return:
        """
        cache = redis.Redis()
        url = args[0]
        count = f"count:{url}"
        data = f"data:{url}"

        cache.incr(count)

        if cache.exists(data):
            return cache.get(data).decode("utf-8")

        result = method(*args, **kwargs)

        cache.setex(data, 10, result)

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
