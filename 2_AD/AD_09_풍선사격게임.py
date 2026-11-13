# AD_09 풍선 사격 게임
# 풀이: "남아 있는 풍선 집합"이 같으면 그 뒤로 얻을 최대 점수도 같다.
#       집합을 비트마스크로 나타내고, 한 번 계산한 값은 memo에 저장한다(메모이제이션).
#       N <= 10 이라 집합은 최대 2^10 = 1024개뿐이다.
import sys
input = sys.stdin.readline


def best_score(mask):
    """mask = 아직 남은 풍선(i번째 비트가 1이면 i번 풍선이 남아 있음).
    여기서부터 끝까지 얻을 수 있는 최대 점수."""
    if mask == 0:                    # 남은 풍선이 없으면 0점
        return 0
    if mask in memo:                 # 이미 계산했으면 저장한 값을 쓴다
        return memo[mask]

    # 남아 있는 풍선 번호를 왼쪽부터 모은다
    alive = []
    for i in range(N):
        if mask & (1 << i):
            alive.append(i)

    result = 0
    for idx in range(len(alive)):
        i = alive[idx]                       # 이번에 터뜨릴 풍선
        has_left = idx > 0                   # 왼쪽 이웃이 있는가
        has_right = idx < len(alive) - 1     # 오른쪽 이웃이 있는가

        if has_left and has_right:
            score = K[alive[idx - 1]] * K[alive[idx + 1]]   # 양쪽: 곱
        elif has_left:
            score = K[alive[idx - 1]]                       # 왼쪽만
        elif has_right:
            score = K[alive[idx + 1]]                       # 오른쪽만
        else:
            score = K[i]                                    # 이웃 없음: 자기 숫자

        total = score + best_score(mask - (1 << i))         # i번을 터뜨린 뒤의 최대 점수
        if total > result:
            result = total

    memo[mask] = result
    return result


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    K = list(map(int, input().split()))
    memo = {}
    all_balloons = (1 << N) - 1      # 처음엔 N개가 모두 남아 있다 (비트 N개가 모두 1)
    print("#" + str(tc) + " " + str(best_score(all_balloons)))
