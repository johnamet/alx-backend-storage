#!/usr/bin/env python3
"""Inserts a new document based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.
    Returns the new _id.
    """
    return mongo_collection.insert_one(kwargs).inserted_id
