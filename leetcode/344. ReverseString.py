'''
Write a function that reverses a string. The input string is given as an array of characters s.

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
'''

# 풀이1 투 포인터를 이용한 스왑
def reverseString(self, s):
    left, right = 0, len(s) -1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# Runtime: 175 ms, faster than 60.71% of Python online submissions for Reverse String.
# Memory Usage: 21.1 MB, less than 55.87% of Python online submissions for Reverse String.

# 풀이2 파이썬다운 방식 (pythonic way)
def reverseString(self, s):
    s.reverse()

# Runtime: 300 ms, faster than 9.71% of Python online submissions for Reverse String.
# Memory Usage: 21.3 MB, less than 14.95% of Python online submissions for Reverse String.