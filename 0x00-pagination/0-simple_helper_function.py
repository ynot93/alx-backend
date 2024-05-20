#!/usr/bin/env python3
"""
This module deals with pagination of datasets

"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    Returns a tuple containing range of pagination params.

    """
    offset = (page - 1) * page_size
    return (offset, offset + page_size)
