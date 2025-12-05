class Solution:
    def countPartitions(self, nums):
        n = len(nums)

        def total_parity():
            # returns 1 if total is odd, 0 if even
            return sum(nums) & 1

        def all_splits_count():
            # number of possible split positions is n-1 (but not less than 0)
            return max(0, n - 1)

        # If total is odd → 0, else all splits are valid
        return 0 if total_parity() else all_splits_count()
