#!/usr/bin/env python3
""" find with specific topic """


def schools_by_topic(mongo_collection, topic):
    """ find with specific topic """
    return mongo_collection.find({"topics": topic})
