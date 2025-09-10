import pytest
from src.analytics import chunk, running_total, index_of_first_at_least


def test_chunk_basic_and_edges():
    assert chunk([1,2,3,4,5], 2) == [[1,2],[3,4],[5]]
    assert chunk([], 3) == []
    with pytest.raises(ValueError):
        chunk([1,2], 0)


def test_running_total():
    assert running_total(10, [-2, 5, -1]) == [8, 13, 12]
    assert running_total(0, []) == []


def test_index_of_first_at_least():
    assert index_of_first_at_least([1,3,5,7], 5) == 2
    assert index_of_first_at_least([1,2,3], 10) is None