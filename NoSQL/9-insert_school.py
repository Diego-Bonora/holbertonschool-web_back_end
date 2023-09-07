#!/usr/bin/env python3
""" insert into colection """


def insert_school(mongo_collection, **kwargs):
    """ insert into colection """
    dict = {}
    for key, value in kwargs.items():
        dict[key] = value
    return mongo_collection.insert(dict)
