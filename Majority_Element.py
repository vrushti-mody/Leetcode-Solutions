# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        di={}
        if len(nums)==1 or len(nums)==2:
            return nums[0]
        for i in nums:
            if i in di:
                di[i]=di[i]+1
                if di[i]>= len(nums)//2 +1:
                    return i
            else:
                di[i]=1
