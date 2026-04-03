import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # [[Car position, time to finish], [Car position, time to finish]...]
        carPosToTimeToFinish = []

        for position, speed in zip(position, speed):
            timeToFinish = (target - position) / speed
            carPosToTimeToFinish.append([position, timeToFinish])

        carPosToTimeToFinish.sort(key=lambda x: x[0], reverse=True)

        fleets = 0
        maxTime = 0

        for car in carPosToTimeToFinish:
            if car[1] > maxTime:
                fleets += 1
                maxTime = car[1]
        
        return fleets
