# Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        return min(abs(30*hour-5.5*minutes),360-abs(30*hour-5.5*minutes))
        
