#!/usr/bin/env python3
"""
This module expounds on Caching concepts

"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Basic Caching system

    """
    def __init__(self):
        """
        Initialize cache object

        """
        super().__init__()

    def put(self, key: str, item: str) -> None:
        """
        Assigns data to the cache

        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

    def get(self, key: str) -> str:
        """
        Retrieve data from cache

        """
        if key is None or key not in self.cache_data:
            return None

        item = self.cache_data.get(key)
        return item
