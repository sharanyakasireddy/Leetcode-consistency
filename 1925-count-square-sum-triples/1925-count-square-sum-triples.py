class Solution:
    def countTriples(self, n: int) -> int:
        squares={i*i: i for i in range(1, n+1)}
        count=0
        for k in range(1,n+1):
            for j in range(1,n+1):
                if k*k + j*j in squares:
                    count+=1
        return count