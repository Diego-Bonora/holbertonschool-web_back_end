#!/usr/bin/env python3
""" updates a document """


def update_topics(mongo_collection, name, topics):
    """ updates a document """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
