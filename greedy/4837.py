A = [i for i in range(1,13)]

T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    # 부분집합 중 원소의 개수 N개
    # 합이 K인 부분집합의 개수
    count = 0

    def comb(cnt, selected, start):
        #원소의 개수가 N개 => 12개 중 3개 고른것과 같음
        global count
        if cnt == N:
            #그 N개의 원소의 합이 K인 것만
            if sum(selected) == K:
                count +=1
            return
        
        for i in range(start, 12):
            comb(cnt+1, selected + [A[i]], i+1)
    comb(0,[],0)        

    print(f'#{tc} {count}')