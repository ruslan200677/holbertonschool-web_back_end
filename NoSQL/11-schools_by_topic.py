#!/usr/bin/env python3
""" 11-main """


def schools_by_topic(mongo_collection, topic):
    """where can i learn python>"""
    return mongo_collection.find({"topics": topic})
