#!/usr/bin/env python3
"""The script contains a Cahce class
that initialises redis"""
import functools
import uuid
from typing import Union, Callable, Optional
import redis


def count_calls(method: Callable) -> Callable:
    """
    A decorator that counts the number of times a
    method has been called
    :param method: The method to be decorated
    :return: The decorated method
    """

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function that increments the
        count and calls the decorated method
        :param self: The instance of the class
        :param args: The arguments of the method
        :param kwargs: The keyword arguments of the method
        :return:  The result of the decorated method
        """

        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """"
    A decorator that stores the history of
    inputs and outputs for a particular method
    :param method: The method to be decorated
    :return: The decorated method
    """

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function that stores the
        history of inputs and outputs for a particular method
        :param self: the instance of the class
        :param args: the arguments of the method
        :param kwargs: the keyword arguments of the method
        :return: the result of the decorated method
        """

        qualname = method.__qualname__
        self._redis.rpush(f'{qualname}:inputs', str(args))

        output = method(self, *args, **kwargs)
        self._redis.rpush(f'{qualname}:outputs', str(output))

        return output

    return wrapper


class Cache:
    """
    A Cache class that stores inputs and outputs for a particular method
    """

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores data in the cache
        :param data: the data to be stored
        :return: str -- the key of the data
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable[[bytes], Union[str, bytes, int, float]]]
            = None) \
            -> Union[str, bytes, int, float, None]:
        """
        Retrieves data from the cache
        :param key: the data key
        :param fn: function to convert data to appropriate type
        :return:
        """

        data = self._redis.get(key)

        if data is None:
            return None

        return fn(self._redis.get(key)) if fn else data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieves data from the cache
        :param key: The data key
        :return: The string value or None if the key does not exist
        """

        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieves data from the cache
        :param key: The data key
        :return: The integer value or None if the key does not exist
        """

        return self.get(key, lambda x: int(x))


def replay(method: Callable):
    """
    A function to display the history of a
    particular function
    :param self: the instance of the class
    :param method: The function to call
    :return:
    """

    redis_instance = method.__self__._redis
    key = method.__qualname__
    calls_count = redis_instance.get(key)
    print(f'{key} was called {int(calls_count)} times:')

    inputs = redis_instance.lrange(f'{key}:inputs', 0, -1)
    outputs = redis_instance.lrange(f'{key}:outputs', 0, -1)

    for i, j in zip(inputs, outputs):
        print(f"{key}(*{i.decode('utf-8')}) -> {j.decode('utf-8')}")
