#!/usr/bin/env python3
"""Inserting documents in collections."""


def insert_school(mongo_collection, **kwargs):
    return mongo_collection.insert_one(kwargs).inserted_id
