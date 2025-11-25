class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()  # to store unique characters
        left = 0      # window start
        max_len = 0   # result

        for right in range(len(s)):
        # If character is already in the current window, move left until it's removed
          while s[right] in seen:
              seen.remove(s[left])
              left += 1
        
          seen.add(s[right])  # Add current character
          max_len = max(max_len, right - left + 1)  # Update max length
    
        return max_len