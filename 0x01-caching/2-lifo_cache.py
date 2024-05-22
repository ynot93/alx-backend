#!/usr/bin/env python3
"""
This module expounds on Caching concepts

"""
from typing import Optional
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    Implements LIFO policy in caching

    """
    def __init__(self):
        """
        Initialize cache object

        """
        super().__init__()
        self.lifo_order = []

    def put(self, key: str, item: str) -> None:
        """
        Assigns data to the cache

        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.lifo_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = self.lifo_order.pop()
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

        self.cache_data[key] = item
        self.lifo_order.append(key)

    def get(self, key: str) -> Optional[str]:
        """
        Retrieve data from cache

        """
        if key is None or key not in self.cache_data:
            return None

        item = self.cache_data.get(key)
        return item
