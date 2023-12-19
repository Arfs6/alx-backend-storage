#!/usr/bin/env python
"""finding documents."""


def schools_by_topic(mongo_collection, topic):
    """Finding documents with topics."""
    # return mongo_collection.find({'topics': {"$elemMatch": {"$eq": topic}}})
    return mongo_collection.find({"topics": topic})
