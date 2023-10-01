import itertools
from typing import Any, List,Generator, Tuple

# From existing List and limit
def batch(data: List[Any], step: int) -> Generator[List[Any], None, None]:
    """
    This function takes a list of input data and breaks it down into smaller batches of a specified size.

    Args:
        data (List[Any]): the input data to be batched
        step (int): the size of each batch

    Yields:
        Generator[List[Any], None, None]: a generator that returns a list of batched data
    """

    _obj_len = len(data)
    if _obj_len:
        starts = itertools.count(step=step)
    else:
        starts = range(0, _obj_len, step)

    for start in starts:
        end = start + step - 1
        if _obj_len is not None:
            end = min(end, _obj_len - 1)
        vals = data[start : end + 1]
        if vals:
            yield vals
        else:
            break

# From a count and limit
def paginate(
    total_count: int, limit: int, start_at_one: bool = True
) -> Generator[Tuple[int, int, int], None, None]:
    """
    A generator function that yields tuples representing page numbers and ranges
    of items within a total count, given a page limit.

    Args:
        total_count (int): The total count of items.
        limit (int): The limit of items to include per page.
        start_at_one (bool, optional): Whether to use 1-based indexing. Defaults to True.

    Yields:
        Tuple[int, int, int]: A tuple containing the page number, start index, and end index of the page range.
    """
    page_num = 1
    while True:
        if page_num == 1:
            start_index = 0
        else:
            start_index = (page_num - 1) * limit
        end_index = min(start_index + limit, total_count)
        if start_at_one:
            yield page_num, start_index + 1, end_index
        else:
            yield page_num, start_index, end_index
        page_num += 1
        if end_index == total_count:
            break