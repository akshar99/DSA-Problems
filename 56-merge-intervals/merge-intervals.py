class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        We have to ceck if two intervals overlap or not 
        that means nums[i-1][1] < nums[i][1] and > nums[i][0]
        better to do it in an empty array as it will be easy to append and check the last element  
        of the array
        '''

        new = []
        intervals.sort(key=lambda x: x[0])

        new.append(intervals[0])

        for i in range(1, len(intervals)):

            if new[-1][1] >= intervals[i][0]:

                new[-1][1] = max(new[-1][1], intervals[i][1])

            else:
                new.append(intervals[i])

        return new