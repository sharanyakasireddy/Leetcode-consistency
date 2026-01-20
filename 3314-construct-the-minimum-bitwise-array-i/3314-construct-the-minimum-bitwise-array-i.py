class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for a in nums:
            if a % 2 == 0:
                ans.append(-1)
                continue
            
            # Mask of trailing 1s
            mask = (a ^ (a + 1)) >> 1
            
            # Subtract the highest bit in the mask
            subtract = 1 << (mask.bit_length() - 1)
            ans.append(a - subtract)
        
        return ans