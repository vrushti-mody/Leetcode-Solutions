# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

# Follow up: Your solution should run in O(log n) time and O(1) space.

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        for i in range(0,n,2):
            if nums[i]!=nums[i+1]:
                return nums[i]
            else:
                if nums[n-1-i]!=nums[n-i-2]:
                    return nums[n-1-i]
        
