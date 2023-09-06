#!/usr/bin/env python3
"""list all documents from mongodb"""
import pymongo


def list_all(mongo_collection):
    return mongo_collection.find()
