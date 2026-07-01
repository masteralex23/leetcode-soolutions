class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        letters_dict = {}
        max_length = 0
        curr_len = 0
        while right < len(s):
            c = s[right]
            letters_dict[c] = letters_dict.get(c, 0) + 1
            curr_len+= 1
            while letters_dict[c] > 1:
                letters_dict[s[left]] -= 1
                left += 1
                curr_len -= 1
            if curr_len > max_length:
                max_length = curr_len
            right += 1
        return max_length
                
