T = int(input())
for tc in range(1,T+1):
    N = int(input())
    ids = list(map(int, input().split()))

    answer = 0

    for i in ids:
        answer ^= i
    print(f'#{tc} {answer}')
