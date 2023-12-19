#!/usr/bin/env python3
"""Updating documents."""


def update_topics(mongo_collection, name, topics):
    """Update documents with name = @name to have topic = @topic."""
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
