class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        ans = 0
        count = 0
        
        for ch in s:
            if ch == '1':
                count += 1        # grow the current block of 1s
            else:
                ans += count * (count + 1) // 2
                ans %= MOD
                count = 0        # reset when '0' appears
        
        # add the last block of 1s (if string ends with 1s)
        ans += count * (count + 1) // 2
        ans %= MOD

        return ans