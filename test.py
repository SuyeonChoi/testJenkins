# import sys
# input = sys.stdin.readline

def solution(n, arr):
    result = [-1] * n
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = arr[stack[-1]]
        stack.append(i)

    # print(" ".join(list(map(str, result))))
    return list(map(int, result))


# N = int(input())
# sequence = list(map(int, input().split()))
# result = solution(N, sequence)
# print(result)


def test_simple_test():
    assert solution(4, [3, 5, 2, 7]) == [5, 7, 8, -1]

