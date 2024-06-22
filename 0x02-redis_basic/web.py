#!/usr/bin/env python3
"""
The script implements an expiring web cache and tracker
"""
import functools
from typing import Callable

import redis
import requests


def cache_and_track(method: Callable) -> Callable:
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

        cached_result = cache.get(data_key)

        if cached_result is not None:
            return cache.get(data_key).decode("utf-8")

        result = method(*args, **kwargs)
        cache.incr(count_key)
        cache.setex(data_key, 10, result)

        return result

    return wrapper


@cache_and_track
def get_page(url: str) -> str:
    """
    Get the page from a url
    :param url: The url to get the page from
    :return: the html of the page
    """
    r = requests.get(url)
    return r.text
