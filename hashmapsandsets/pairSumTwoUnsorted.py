from typing import List


def pair_sum_two_unsorted_two_pass(nums: List[int], target: int) -> List[int]:
    num_map = []
    for i, num in enumerate(nums):
        num_map[i] = num
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [i, num_map.index(complement)]
    return []