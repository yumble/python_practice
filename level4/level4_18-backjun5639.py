import sys

sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

nums = []

while True:
    try:
        nums.append(int(input()))
    except:
        break

def postorder(start, end):

    if start > end:
        return
    mid = end + 1  # 오른쪽 노드가 없을 경우

    for i in range(start + 1, end + 1):
        if nums[start] < nums[i]:
            mid = i
            break

    postorder(start + 1, mid - 1)
    postorder(mid, end)
    print(nums[start])

postorder(0, len(nums) - 1)
