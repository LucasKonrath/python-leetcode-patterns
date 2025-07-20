from typing import List


def zero_striping_sets(matrix: List[List[int]]) -> None:
    if not matrix or not matrix[0]:
        return

    rows, cols = len(matrix), len(matrix[0])
    zero_rows = set()
    zero_cols = set()

    # First pass: identify rows and columns that need to be zeroed
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                zero_rows.add(r)
                zero_cols.add(c)

    # Second pass: zero out identified rows and columns
    for r in range(rows):
        for c in range(cols):
            if r in zero_rows or c in zero_cols:
                matrix[r][c] = 0

