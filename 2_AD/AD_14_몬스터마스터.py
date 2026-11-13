# AD_14 몬스터 마스터
# 풀이: 방문 순서를 전부 해 본다(DFS). 단, 몬스터 k를 잡은 뒤에만 의뢰인 -k에게 갈 수 있다.
#       장애물이 없으므로 두 지점 사이 시간 = |행 차이| + |열 차이| (맨해튼 거리)
import sys
input = sys.stdin.readline


def distance(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)


def dfs(r, c, time, finished):
    """지금 (r, c)에 있고 time만큼 걸렸고, 전달을 finished번 끝냈다."""
    global best
    if time >= best:                     # 이미 최선보다 느리면 더 볼 필요 없음(가지치기)
        return
    if finished == len(kinds):           # 모두 전달했으면 기록
        best = time
        return

    for k in kinds:
        if not caught[k]:
            # 아직 안 잡은 몬스터 k를 잡으러 간다
            mr, mc = monster_pos[k]
            caught[k] = True
            dfs(mr, mc, time + distance(r, c, mr, mc), finished)
            caught[k] = False            # 되돌리기
        elif not delivered[k]:
            # 잡았지만 아직 전달 안 한 의뢰인 k에게 간다
            cr, cc = client_pos[k]
            delivered[k] = True
            dfs(cr, cc, time + distance(r, c, cr, cc), finished + 1)
            delivered[k] = False         # 되돌리기


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    monster_pos = {}     # 몬스터 번호 -> 위치
    client_pos = {}      # 의뢰인 번호(양수로 바꿔서) -> 위치
    for r in range(N):
        row = list(map(int, input().split()))
        for c in range(N):
            if row[c] > 0:
                monster_pos[row[c]] = (r, c)
            elif row[c] < 0:
                client_pos[-row[c]] = (r, c)

    kinds = list(monster_pos.keys())     # 이번 마을에 있는 몬스터 번호들
    caught = {}
    delivered = {}
    for k in kinds:
        caught[k] = False
        delivered[k] = False

    best = 999999999
    dfs(0, 0, 0, 0)
    print("#" + str(tc) + " " + str(best))
