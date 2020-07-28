# Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums=sorted(nums)
        
        li=[]
        
        for i in range(0, len(nums)):
            if i==0:
                if nums[i]!=nums[i+1]:
                    li.append(nums[i])
            elif i==len(nums)-1:
                if nums[i]!=nums[i-1]:
                    li.append(nums[i])
            else:
                if nums[i]!=nums[i-1] and nums[i]!=nums[i+1]:
                    li.append(nums[i])
                
        return li
