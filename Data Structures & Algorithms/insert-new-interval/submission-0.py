class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # add intervals to answer
        answer = []
        hasBeenAdded = False
        for i in range(len(intervals)):
            # case 1: newinterval starts and ends before current interval
            if not hasBeenAdded and newInterval[0] < intervals[i][0] and newInterval[1] < intervals[i][0]:
                # add newinterval
                answer.append(newInterval)
                hasBeenAdded = True
                answer.append(intervals[i])
            # case 2: new interval overlaps with curr interval
            elif (newInterval[1] >= intervals[i][0] and newInterval[0] <= intervals[i][1]) or (newInterval[0] <= intervals[i][1] and newInterval[1] >= intervals[i][0]):
                # change new Interval to new overlap
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
            # case 3: new interval starts after current interval
            elif hasBeenAdded or newInterval[0] > intervals[i][1]:
                # add current interval
                answer.append(intervals[i])
        print(newInterval)
        if not hasBeenAdded:
            answer.append(newInterval)
        return answer
        