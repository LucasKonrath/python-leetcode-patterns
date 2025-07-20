from typing import List


def largest_container_brute_force(heights: List[int]) -> int:
    n = len(heights)
    max_water = 0
    for i in range(n):
        for j in range(i + 1, n):
            water = min(heights[i], heights[j]) * (j - i)
            max_water = max(max_water, water)
    return max_water

def largest_container_two_pointers(heights: List[int]) -> int:
    left, right = 0, len(heights) - 1
    max_water = 0
    while left < right:
        water = min(heights[left], heights[right]) * (right - left)
        max_water = max(max_water, water)
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return max_water