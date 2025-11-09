class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in range(len(nums2)):
            nums1.append(nums2[i])
        nums1.sort()
        l=len(nums1)//2
        if len(nums1)%2==0:
            ans=(nums1[l-1]+nums1[l])/2
        else:
            ans=nums1[l]
        return ans
        