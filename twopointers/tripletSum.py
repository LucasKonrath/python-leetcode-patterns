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