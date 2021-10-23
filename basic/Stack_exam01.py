# exam1 괄호 맞추기
# -(2+5)*7-((3-1)/2 +7)

# 문제 입력 : 왼쪽, 오른쪽 괄호의 문자열
# 문제 출력 : 괄호 쌍이 맞춰져 있으면 True, 아니면 False

# 예1 : (()()) 122331
# 예2 : ()) 112
# 예3 : ()( 112

def solution(s):
    d = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }
    stack = []
    for c in s:
        if c in '({[':
            stack.append(c)
        elif c in ')}]':
            if stack:
                top = stack.pop()
                if d[c] != top:
                    return False
            else:
                return False
    return len(stack) == 0