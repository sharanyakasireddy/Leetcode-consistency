class Solution:
    def countPartitions(self, nums):
        n = len(nums)

        def total_parity():
            return sum(nums) & 1

        def all_splits_count():
            return max(0, n - 1)

        return 0 if total_parity() else all_splits_count()
