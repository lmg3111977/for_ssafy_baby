# SWEA 1267 [S/W 문제해결 응용] 10일차 - 작업순서
# 문제: 작업 V개와 "a를 해야 b를 할 수 있다"는 선행 관계 E개. 가능한 작업 순서 하나를 출력.
#       테스트 케이스는 항상 10개(T 줄이 없다).
# 풀이: 위상 정렬. 선행 작업이 남지 않은(진입 차수 0) 작업부터 큐에 넣고,
#       하나 끝낼 때마다 그 뒤 작업들의 진입 차수를 1씩 줄인다.
from collections import deque

for tc in range(1, 11):
    V, E = map(int, input().split())
    pairs = list(map(int, input().split()))      # a1 b1 a2 b2 ... 한 줄로 주어짐

    after = []                   # after[a] = a를 끝내야 할 수 있는 작업들
    for i in range(V + 1):
        after.append([])
    indegree = [0] * (V + 1)     # indegree[b] = b보다 먼저 해야 하는 작업 수
    for i in range(E):
        a = pairs[2 * i]
        b = pairs[2 * i + 1]
        after[a].append(b)
        indegree[b] = indegree[b] + 1

    queue = deque()
    for v in range(1, V + 1):
        if indegree[v] == 0:
            queue.append(v)

    order = []
    while len(queue) > 0:
        v = queue.popleft()
        order.append(v)
        for nxt in after[v]:
            indegree[nxt] = indegree[nxt] - 1
            if indegree[nxt] == 0:             # 선행 작업이 다 끝났으면 할 수 있다
                queue.append(nxt)

    text = "#" + str(tc)
    for v in order:
        text = text + " " + str(v)
    print(text)
