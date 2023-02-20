#!/usr/bin/env python3
from typing import Tuple
''' Description: Write a function named index_range that takes two integer
                 arguments page and page_size.
                 The function should return a tuple of size two containing
                 a start index and an end index corresponding to the range
                 of indexes to return in a list for those particular
                 pagination parameters.
    Page numbers are 1-indexed, i.e. the first page is page 1.
'''

def index_range(page: int, page_size: int) -> Tuple[int, int]:
  """_summary_

  Args:
      page (int): _Current Page_
      page_size (int): _Numbers of items on per page _

  Returns:
      Tuple[int, int]: _Current items, The end of items_
  """
    return ((page_size * (page - 1)), page_size * page)
