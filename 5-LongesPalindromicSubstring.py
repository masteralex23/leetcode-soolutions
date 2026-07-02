class Solution:
    def longestPalindrome(self, s: str) -> str:
        current_palindrome = ""
        longest_palindrome = ""
        for i, c in enumerate(s):
            current_palindrome = c
            j = i-1
            k = i+1
            while i > 0 and c == s[i-1]:
                current_palindrome = s[i-1] + current_palindrome
                i-=1
                j-=1
            while j >= 0 and k < len(s) and s[j] == s[k]:
                current_palindrome = s[j] + current_palindrome + s[k]
                j-= 1
                k+= 1
            if len(current_palindrome) > len(longest_palindrome):
                longest_palindrome = current_palindrome
        return longest_palindrome