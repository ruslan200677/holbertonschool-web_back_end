#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""
import csv
from typing import List, Dict
import os


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = os.path.join(
        os.path.dirname(__file__), "Popular_Baby_Names.csv"
    )

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header row
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return a dictionary with pagination
        data and ensure deletions are handled."""
        assert index is not None and index >= 0, "index must be non-negative"

        indexed_dataset = self.indexed_dataset()
        assert index < len(indexed_dataset), "index out of range"

        data = []
        current_index = index
        for _ in range(page_size):
            while current_index not in indexed_dataset:
                current_index += 1
                if current_index >= len(indexed_dataset):
                    break
            if current_index >= len(indexed_dataset):
                break
            data.append(indexed_dataset[current_index])
            current_index += 1

        next_index = current_index
        return {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": next_index,
        }
