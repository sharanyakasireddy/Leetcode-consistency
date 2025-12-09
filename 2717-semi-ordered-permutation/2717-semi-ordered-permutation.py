class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n=len(nums)
        i=nums.index(1)
        j=nums.index(n)
        x=i+(n-1-j)
        if i>j:x-=1
        return x