#!/usr/bin/env python3
"""
This module expounds on Caching concepts

"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    Implements MRU policy in caching

    """
    def __init__(self):
        """
        Initialize cache object

        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key: str, item: str) -> None:
        """
        Assigns data to the cache

        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.pop(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            most_recent_key, _ = self.cache_data.popitem(last=True)
            print(f"DISCARD: {most_recent_key}")

        self.cache_data[key] = item

    def get(self, key: str) -> str:
        """
        Retrieve data from cache

        """
        if key is None:
            return None

        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]

        return None
