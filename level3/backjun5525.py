# n = int(input())
# s = int(input())
# str = input()
# count, tmp, nowI = 0, 0, True
#
# def isI(c):
#     if c == 'I':
#         return True
#     return False
#
# for c in str:
#     if isI(c) and nowI:
#         tmp += 1
#         nowI = False
#     elif not isI(c) and not nowI:
#         tmp += 1
#         nowI = True
#     elif isI(c) and not nowI:
#         tmp = 1
#         nowI = False
#     else:
#         tmp = 0
#         nowI = True
#     if tmp == 2*n + 1:
#         count += 1
#         tmp -= 2
#         nowI = False
# print(count)
#


n = int(input())
m = int(input())
s = input().rstrip()

# 투 포인터 알고리즘
left, right = 0, 0
cnt = 0

while right < m: # m 범위 내에서 반복
    # 3개 슬라이싱한 것이 'IOI'인 경우
    if s[right:right + 3] == 'IOI':
        right += 2 # 오른쪽 두 칸 이동
        # 길이 조건을 만족하는 경우
        if right - left == 2 * n:
            # 카운트하고 오른쪽으로 두 칸 이동
            cnt += 1
            left += 2
    else: # 조건 만족하지 않는 경우
        # 오른쪽으로 한 칸 이동
        right += 1
        left = right

print(cnt)