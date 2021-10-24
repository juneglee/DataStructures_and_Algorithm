"""
Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.


Constraints:

1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters.
"""
# 주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다
# 참고 : 팰린드롬이란? 앞뒤가 똑같은 단어나 문장으로, 뒤집어도 같은 말이 되는 단어 또는 문장을 팰린드롬이라고 한다
#

# 풀이1 리스트로 변환
def isPalindrome(self,s):
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    # 팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True

# Runtime: 675 ms, faster than 14.59% of Python online submissions for Valid Palindrome.
# Memory Usage: 15.2 MB, less than 36.16% of Python online submissions for Valid Palindrome.

# 풀이2 데크 자료형을 이용한 최적화
# def isPalindrome(self, s):
#     # 자료형 데크로 선언
#     strs: Deque = collections.deque()
#
#     for char in s:
#         if char.isalnum():
#             strs.append(char.lower())
#
#     while len(strs) > 1:
#         if strs.popleft != strs.pop():
#             return False
#
#     return True

# 풀이3 슬라이싱 사용
def isPalindrome(self, s):
    s = s.lower()
    # 정규식으로 불필요한문자 필터링
    s = re.sub('[^a-z0-9]', '', s)

    return s ==s[::-1] # 슬라이싱

# Runtime: 20 ms, faster than 99.76% of Python online submissions for Valid Palindrome.
# Memory Usage: 15.9 MB, less than 13.81% of Python online submissions for Valid Palindrome.