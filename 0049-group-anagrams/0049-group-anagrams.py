from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict=defaultdict(list)
        for i in range(len(strs)):
            a=strs[i]
            b=tuple(sorted(strs[i]))
            my_dict[b].append(a) 
        ans=tuple(my_dict.values())
        return ans