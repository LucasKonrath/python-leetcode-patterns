from typing import List


## O(n3)
def bruteForceTripletSum(nums: List[int]):
    n = len(nums)
    triplets = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = tuple(sorted((nums[i], nums[j], nums[k])))
                    triplets.add(triplet)
    return [list(triplet) for triplet in triplets]

def tripletSumSorted(nums: List[int]) -> List[List[int]]:
    triplets = set()
    nums.sort()
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        pairs = pair_sum_sorted_all_pairs(nums, i + 1, -nums[i])
        for pair in pairs:
            triplet = tuple([nums[i]] + pair)
            triplets.add(triplet)
    return [list(triplet) for triplet in triplets]

def pair_sum_sorted_all_pairs(nums: List[int], start: int, target: int) -> List[List[int]]:
    pairs = []
    left, right = start, len(nums) - 1
    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            pairs.append([nums[left], nums[right]])
            left += 1
            right -= 1
            while left < right and nums[left] == nums[left - 1]:
                left += 1
            while left < right and nums[right] == nums[right + 1]:
                right -= 1
        elif sum < target:
            left += 1
        else:
            right -= 1
    return pairs