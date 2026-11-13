# AD_21 화분 키우기
# 풀이: DP. 각 화분까지의 최대 합을 "이 화분에 준 비료 종류"별로 기억한다.
#   dp1 = 지금 화분에 비료 1을 줬을 때 여기까지 최대 합
#   dp2 = 지금 화분에 비료 2를 줬을 때 여기까지 최대 합
# 주의: 덜 자라도 높이가 음수가 되지는 않는다 -> max(0, 높이 - p)
#       (5 - 19 = -14가 아니라 0. 이걸 빼먹으면 오답!)
import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T + 1):
    n, p = map(int, input().split())
    grow1 = list(map(int, input().split()))   # 비료 1을 줬을 때 자라는 높이
    grow2 = list(map(int, input().split()))   # 비료 2를 줬을 때 자라는 높이

    # 첫 번째 화분: 왼쪽 화분이 없으니 감소 없음
    dp1 = grow1[0]
    dp2 = grow2[0]

    for i in range(1, n):
        # 이번 화분에 비료 1을 준다
        same = dp1 + max(0, grow1[i] - p)     # 왼쪽도 비료 1 -> 같은 비료 연속, p 감소
        different = dp2 + grow1[i]            # 왼쪽은 비료 2 -> 감소 없음
        new_dp1 = max(same, different)

        # 이번 화분에 비료 2를 준다
        same = dp2 + max(0, grow2[i] - p)
        different = dp1 + grow2[i]
        new_dp2 = max(same, different)

        dp1 = new_dp1
        dp2 = new_dp2

    print("#" + str(tc) + " " + str(max(dp1, dp2)))
