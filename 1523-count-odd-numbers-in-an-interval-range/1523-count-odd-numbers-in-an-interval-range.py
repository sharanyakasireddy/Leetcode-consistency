class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = (high - low) // 2
        if low % 2 == 1 or high % 2 == 1:
            count += 1
        return count
        
        
        
        #if low%2==1 and high%2==1:
        #    diff=high-low+1
        #    return diff//2+1
        #else:
        #   diff=high-low+1
        #    return diff//2