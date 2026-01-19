class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []

        for num in range(left, right + 1):
            x = num
            is_valid = True

            while x > 0:
                digit = x % 10
                if digit == 0 or num % digit != 0:
                    is_valid = False
                    break
                x //= 10

            if is_valid:
                res.append(num)

        return res