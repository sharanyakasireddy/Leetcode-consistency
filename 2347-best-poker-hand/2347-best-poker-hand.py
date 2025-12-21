from collections import Counter
from typing import List

class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits))==1:
            return "Flush"
        
        freq=Counter(ranks)
        max_count=max(freq.values())
        
        if max_count>=3:
            return "Three of a Kind"
        elif max_count==2:
            return "Pair"
        else:
            return "High Card"

        