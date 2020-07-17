# Given a non-empty array of integers, return the k most frequent elements.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        number_frequency = {}
        frequency_list ={}
        for i in nums:
            if i not in number_frequency:
                number_frequency[i] = 1
            else:
                number_frequency[i] += 1
        for key,value in number_frequency.items():
            if value not in frequency_list:
                frequency_list[value] = [key]
            else:
                frequency_list[value].append(key)
        result = []
        for i in range(len(nums),0,-1):
            if i in frequency_list:
                result.extend(frequency_list[i])
            if len(result) >=k:
                break
        return result
                
