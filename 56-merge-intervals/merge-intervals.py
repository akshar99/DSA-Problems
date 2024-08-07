class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        print('Sorted intervals')

        merged = [intervals[0]]

        for current in intervals[1:]:
            last = merged[-1]
            print(merged[-1])
            
            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])
            else:
                merged.append(current)


        return merged
        
        
        
        
        
        
        
        """
        First Failed Soln 
        XD
        st_out = []
        for i in range(1, len(intervals)):
            if intervals[i-1][1] > intervals[i][0] or intervals[i-1][1] == intervals[i][0]:
                st_out.append([intervals[i-1][0], intervals[i][1]])
            """