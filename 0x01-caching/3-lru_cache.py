#!/usr/bin/env python3
"""
This module expounds on Caching concepts

"""
BaseCaching = __import__('base_caching').BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    Implements LRU policy in caching

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
            self.cache_data.move_to_end(key)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lru_key = next(iter(self.cache_data))
            del self.cache_data[lru_key]
            print(f"DISCARD {lru_key}")

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
