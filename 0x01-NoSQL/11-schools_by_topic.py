#!/usr/bin/env python3
""" schools by topic """


def schools_by_topic(mongo_collection, topic):
    """Returns scools by topic"""
    return list(mongo_collection.find({"topics": topic}))
