# 2에서 9까지 숫자가 주어졌을 때 전화 번호로 조합 가능한 모든 문자를 출력하라.
'''
Given a string containing digits from 2-9 inclusive,
 return all possible letter combinations that the number could represent.
Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
'''
# 2는 abc, 3은 def가 가능하므로 각각 한 문자씩 9개의 문자로 조합이 가능하다

# digits 는 입력값
# 각 자릿수에 해당하는 키판 배열을 DFS로 탐색
def letterCombinations(self, digits):
    def dfs(index, path):
        # 입력값을 자릿수로 쪼개어 반복하고, 숫자에 해당하는 모든 문자열을 반복하면서 마찬가지로 문자 단위로 재귀 탐색
        # 끝까지 탐색하면 백트래킹
        if len(path) == len(digits):
            result.append(path)
            return
        
        # 입력값 자릿수 단위 반복
        for i in range(index, len(digits)):
            # 숫자에 해당하는 모든 문자열 반복
            for j in dic[digits[i]]:
                dfs(i + 1, path + j)
    # 예외 처리
    if not digits:
        return []

    # 키판 배열
    dic = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    result = []
    dfs(0, "")

    return result

# Runtime: 20 ms, faster than 62.10% of Python online submissions for Letter Combinations of a Phone Number.
# Memory Usage: 13.4 MB, less than 70.01% of Python online submissions for Letter Combinations of a Phone Number.