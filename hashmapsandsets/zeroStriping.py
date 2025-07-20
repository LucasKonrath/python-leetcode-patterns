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

def zero_striping_in_place(matrix: List[List[int]]) -> None:
    if not matrix or not matrix[0]:
        return

    rows, cols = len(matrix), len(matrix[0])
    first_row_zeroed = False
    for c in range(cols):
        if matrix[0][c] == 0:
            first_row_zeroed = True
            break

    first_col_zeroed = False
    for r in range(rows):
        if matrix[r][0] == 0:
            first_col_zeroed = True
            break
    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                matrix[r][0] = 0

    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0

    if first_row_zeroed:
        for c in range(cols):
            matrix[0][c] = 0

    if first_col_zeroed:
        for r in range(rows):
            matrix[r][0] = 0