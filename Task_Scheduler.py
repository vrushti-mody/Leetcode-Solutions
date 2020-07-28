# You are given a char array representing tasks CPU need to do. It contains capital letters A to Z where each letter represents a different task. Tasks could be done without the original order of the array. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

# However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

# You need to return the least number of units of times that the CPU will take to finish all the given tasks.

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        char_freq = sorted(Counter(tasks).values() , reverse = True)
        index , counter , max_freq = 0 , 0 , char_freq[0]
        while index < len(char_freq) and char_freq[index] == max_freq:
            counter += 1
            result = (max_freq - 1) * (n + 1) + counter
            index += 1
        return max(result , len(tasks))
        
