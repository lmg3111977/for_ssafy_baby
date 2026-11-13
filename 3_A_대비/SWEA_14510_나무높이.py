# SWEA 14510 나무 높이
# 문제: 홀수 날에 물을 주면 +1, 짝수 날에 주면 +2 (하루에 나무 1그루, 안 줘도 됨).
#       모든 나무를 처음 가장 큰 나무 키로 맞추는 최소 날짜
# 풀이: 날짜 D를 0부터 늘려 가며 "D일이면 가능한가?"를 확인한다.


def is_possible(days, need_one, need_two):
    """days일 동안 +1을 (days+1)//2번, +2를 days//2번 쓸 수 있다. 다 채울 수 있으면 True.
    need_one: 꼭 +1이 한 번 필요한 나무 수 (모자란 키가 홀수인 나무)
    need_two: 나머지를 +2로 채울 때 필요한 +2 횟수"""
    one_count = (days + 1) // 2      # 홀수 날 수: 1, 3, 5, ...
    two_count = days // 2            # 짝수 날 수: 2, 4, 6, ...

    if two_count >= need_two:
        # +2가 충분하다 -> +1만 충분하면 된다
        return one_count >= need_one
    else:
        # +2가 모자라다 -> 모자란 +2 하나는 +1 두 번으로 대신한다
        lack = need_two - two_count
        return one_count >= need_one + lack * 2


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    heights = list(map(int, input().split()))

    tallest = max(heights)
    need_one = 0
    need_two = 0
    for h in heights:
        diff = tallest - h               # 이 나무가 더 자라야 하는 양
        need_one = need_one + diff % 2   # 홀수면 +1이 꼭 한 번 필요
        need_two = need_two + diff // 2  # 나머지는 +2로

    days = 0
    while not is_possible(days, need_one, need_two):   # 불가능하면 하루 늘린다
        days = days + 1

    print("#" + str(tc) + " " + str(days))
