#!/usr/bin/env python3
"""
This module expounds on Caching concepts

"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    def __init__(self):
        """
        Initialize the LFUCache

        """
        super().__init__()
        self.cache_data = {}
        self.usage_frequency = {}
        self.access_order = OrderedDict()

    def put(self, key, item):
        """
        Add an item in the cache with LFU eviction

        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.usage_frequency[key] += 1
            self.access_order.move_to_end(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.evict_lfu()
            self.cache_data[key] = item
            self.usage_frequency[key] = 1
            self.access_order[key] = item

    def get(self, key):
        """
        Get an item by key

        """
        if key is None or key not in self.cache_data:
            return None

        self.usage_frequency[key] += 1
        self.access_order.move_to_end(key)
        return self.cache_data[key]

    def evict_lfu(self):
        """
        Evict the least frequently used item

        """
        if not self.cache_data:
            return

        min_freq = min(self.usage_frequency.values())
        candidates = [k for k, freq in self.usage_frequency.items() if freq == min_freq]
        
        if candidates:
            lru_key = None
            for key in self.access_order:
                if key in candidates:
                    lru_key = key
                    break

            if lru_key:
                del self.cache_data[lru_key]
                del self.usage_frequency[lru_key]
                self.access_order.pop(lru_key)
                print(f"DISCARD: {lru_key}")
