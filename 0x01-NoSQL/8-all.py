#!/usr/bin/env python3
"""Listing all mongo documents."""


def list_all(mongo_collection):
    """Return all documents in collection."""
    return mongo_collection.find()
