#!/usr/bin/env python3
"""
This module deals with pagination of datasets

"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    Returns a tuple containing range of pagination params.

    """
    offset = (page - 1) * page_size
    return (offset, offset + page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns specific page of the dataset

        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        first, last = index_range(page, page_size)
        dataset = self.dataset()

        if first >= len(dataset):
            return []

        return dataset[first:last]
    
    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Returns dataset with hypermedia metadata.

        """
        data = self.get_page(page, page_size)
        dataset_length = len(self.dataset())
        total_pages = math.ceil(dataset_length/page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        metadata = {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }

        return metadata
