class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        total = 0

        for i in range(len(timeSeries) - 1):
            difference = timeSeries[i + 1] - timeSeries[i]

            if difference < duration:
                total += difference
            else:
                total += duration

        total += duration

        return total
