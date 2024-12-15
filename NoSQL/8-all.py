#!/usr/bin/env python3
"""Module"""


def list_all(mongo_collection):
    """List all elements"""
    return list(mongo_collection.find())
