import sys
input = sys.stdin.readline

def solution(n, arr):
    result = [-1] * n
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = arr[stack[-1]]
        stack.append(i)
    return list(map(int, result))

# def test_simple1():
#     assert solution(4, [3, 5, 2, 7]) == [5, 7, 7, -1]


def test_simple2():
    assert solution(4, [3, 5, 2, 7]) == [5, 7, 8, -1], "elements are different"


