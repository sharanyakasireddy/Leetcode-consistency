class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time=0
        for t in range(1,len(points)):
            x1,y1=points[t-1]
            x2,y2=points[t]
            time+=max(abs(x2-x1),abs(y2-y1))
        return time