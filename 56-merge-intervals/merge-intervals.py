class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        new = []

        intervals.sort(key=lambda x: x[0])

        new.append(intervals[0])

        for i in range(1, len(intervals)):

            if new[-1][1] >= intervals[i][0]:

                new[-1][1] = max(new[-1][1], intervals[i][1])

            else:
                new.append(intervals[i])

        return new 
