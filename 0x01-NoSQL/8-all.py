#!/usr/bin/env python3
"""Lists all documents in a collection"""


def list_all(mongo_collection):
    """
    List all documents in a collection
    Returns an empty lsit if o document in the collection
    """

    return list(mongo_collection.find())
