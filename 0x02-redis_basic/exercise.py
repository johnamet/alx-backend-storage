#!/usr/bin/env python3
"""The script contains a Cahce class that initialises redis"""
import uuid

import redis


class Cache:
    def __init__(self):
        self._redis = redis.Redis()

    def flushdb(self):
        """
        Flushes all cached data
        :return:
        """
        self._redis.flushdb()

    def store(self, data: str | bytes | int | float) -> str:
        """
        Stores data in the cache
        :param data: the data to be stored
        :return: str -- the key of the data
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key
