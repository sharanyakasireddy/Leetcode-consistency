class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        Mx = [31,28,31,30,31,30,31,31,30,31,30,31]

        def conv(t):
            mm = int(t[:2])
            dd = int(t[3:])
            s = dd
            k = 0
            
            while k < mm-1:
                s += Mx[k]
                k += 1
            return s

        a1 = conv(arriveAlice)
        a2 = conv(leaveAlice)
        b1 = conv(arriveBob)
        b2 = conv(leaveBob)

        hit = 0
        cur = 1

        trashA = a1 + b2  
        trashB = a2 - b1  

        while cur <= 365:
            aa = (cur >= a1) and (cur <= a2)
            bb = (cur >= b1) and (cur <= b2)
            if aa and bb:
                hit += 1
            cur += 1

        return hit