class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7  # LeetCode asks mod 1e9+7 (problem text notes large answers)
        
        from collections import Counter
        cnt_y = Counter(y for x, y in points)
        
        # m[y] = C(cnt_y, 2)
        m_values = []
        for y, c in cnt_y.items():
            if c >= 2:
                # compute nC2
                m_values.append(c * (c - 1) // 2)
        
        if not m_values:
            return 0
        
        # sum of m[y]
        s = sum(m_values) % MOD
        # sum of squares
        ssq = sum((v * v) % MOD for v in m_values) % MOD
        
        # total = (s^2 - ssq) / 2  (modular division by 2 -> multiply by inv2)
        inv2 = (MOD + 1) // 2
        ans = ( (s * s - ssq) % MOD ) * inv2 % MOD
        return ans
