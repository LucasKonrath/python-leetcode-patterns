from typing import List


def pair_sum_two_unsorted_two_pass(nums: List[int], target: int) -> List[int]:
    num_map = {}
    for i, num in enumerate(nums):
        num_map[num] = i
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map and num_map[complement] != i:
            return [i, num_map[complement]]
    return []

def pair_sum_two_unsorted_one_pass(nums: List[int], target: int) -> List[int]:
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []