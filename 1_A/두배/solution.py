T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    total = sum(A)
    gains = []
    for i in range(1, N + 1):
        new = max(A[i - 1] + i, i)      # 작업 후 값
        gains.append(new - A[i - 1])    # 합이 늘어나는 양
    gains.sort(reverse=True)
    count = 0
    for g in gains:
        if total >= 2 * N:
            break
        total += g
        count += 1
    print(f"#{tc} {count}")
