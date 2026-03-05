T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    print(f"#{tc} {'ON' if M & ((1 << N) - 1) == (1 << N) - 1 else 'OFF'}")
