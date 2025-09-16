from typing import List, Optional

def chunk(lst: List[int], size: int) -> List[List[int]]:
    if size <= 0:
        raise ValueError("size must be positive")
    result = []
    for i in range(0, len(lst), size):
        result.append(lst[i:i+size])
    return result

def running_total(start: int, changes: List[int]) -> List[int]:
    total = start
    result = []
    for c in changes:
        total += c
        result.append(total)
    return result

def index_of_first_at_least(lst: List[int], target: int) -> Optional[int]:
    for i, v in enumerate(lst):
        if v >= target:
            return i
    return None
