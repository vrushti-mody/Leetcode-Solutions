# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

import itertools 

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        li=[]
        for n in range(0,len(nums)+1):
            for i in itertools.combinations(nums, n):
                li.append(list(i))
        return li
