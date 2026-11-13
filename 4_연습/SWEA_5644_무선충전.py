# SWEA 5644 무선 충전
# 문제: 10 x 10 지도에서 사용자 A는 (1,1), B는 (10,10)에서 출발해 정해진 대로 움직인다.
#       매 초 범위 안의 충전기(BC) 하나에 접속해 충전량 P를 얻는다. 둘이 같은 BC면 P를 나눠 갖는다.
#       0초 ~ M초 충전량 합의 최댓값.
# 풀이: 매 초 A가 쓸 수 있는 BC, B가 쓸 수 있는 BC를 구하고
#       (A의 선택, B의 선택) 모든 쌍을 비교한다. 같은 BC를 고르면 합은 P 한 번.

# 이동: 0 제자리, 1 위, 2 오른쪽, 3 아래, 4 왼쪽  (x = 가로, y = 세로)
DX = [0, 0, 1, 0, -1]
DY = [0, -1, 0, 1, 0]


def usable(x, y):
    """(x, y)에서 접속할 수 있는 BC 번호 목록."""
    result = []
    for i in range(A):
        bx, by, cover, power = bcs[i]
        if abs(x - bx) + abs(y - by) <= cover:
            result.append(i)
    return result


def best_charge(ax, ay, bx, by):
    """지금 위치에서 두 사람이 얻을 수 있는 충전량 합의 최댓값."""
    list_a = usable(ax, ay) + [-1]          # -1 = 아무 BC도 안 씀
    list_b = usable(bx, by) + [-1]
    best = 0
    for i in list_a:
        for j in list_b:
            if i == j and i != -1:           # 같은 BC: P를 나눠 가지므로 합은 P
                total = bcs[i][3]
            # 주의: 둘 다 -1(안 씀)일 때 위 조건에 걸리면 bcs[-1] = 마지막 BC가 더해진다(실제로 낸 오답)
            else:
                total = 0
                if i != -1:
                    total = total + bcs[i][3]
                if j != -1:
                    total = total + bcs[j][3]
            if total > best:
                best = total
    return best


T = int(input())
for tc in range(1, T + 1):
    M, A = map(int, input().split())
    move_a = list(map(int, input().split()))
    move_b = list(map(int, input().split()))
    bcs = []
    for i in range(A):
        x, y, c, p = map(int, input().split())
        bcs.append((x, y, c, p))

    ax, ay = 1, 1
    bx, by = 10, 10
    total = best_charge(ax, ay, bx, by)      # 0초(출발 위치)도 충전한다
    for t in range(M):
        ax = ax + DX[move_a[t]]
        ay = ay + DY[move_a[t]]
        bx = bx + DX[move_b[t]]
        by = by + DY[move_b[t]]
        total = total + best_charge(ax, ay, bx, by)

    print("#" + str(tc) + " " + str(total))
