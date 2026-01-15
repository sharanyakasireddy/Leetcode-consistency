class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def max_consecutive_gap(arr: List[int]) -> int:
            arr.sort()
            max_len=1
            current_len=1
            for i in range(1,len(arr)):
                if arr[i]==arr[i-1]+1:
                    current_len+=1
                    max_len=max(max_len,current_len)
                else:
                    current_len=1
            return max_len+1
        max_h_gap=max_consecutive_gap(hBars)
        max_v_gap=max_consecutive_gap(vBars)
        side=min(max_h_gap,max_v_gap)
        return side*side