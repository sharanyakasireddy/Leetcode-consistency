class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # Variables to track max reach, current jump end, and the number of jumps
        maxReach = 0
        currentEnd = 0
        jumps = 0
        
        # We don't need to jump if there's only one element
        for i in range(n - 1):  # No need to check the last element
            # Update maxReach with the farthest we can reach from index i
            maxReach = max(maxReach, i + nums[i])
            
            # If we've reached the end of the current jump's range
            if i == currentEnd:
                jumps += 1  # Increment the number of jumps
                currentEnd = maxReach  # Move the end of the current jump to maxReach
                
                # If the currentEnd exceeds or reaches the last index, we are done
                if currentEnd >= n - 1:
                    break
        
        return jumps
        