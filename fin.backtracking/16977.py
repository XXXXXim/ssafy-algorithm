T = int(input())
for tc in range(1, T + 1):
    N, *lst = map(int, input().split())

    # 최소 충전 횟수를 저장할 변수. N의 최대값이 100이므로 101로 초기화한다.
    min_count = 101

    # 백트래킹
    # idx : 현재 버스정류장 인덱스
    # cnt : 현재 idx 정류장까지 오는데 교체한 배터리 횟수
    def backtracking(idx, cnt):
        global min_count
        
        # 0. 가지치기 (Pruning)
        # 지금까지 교체한 횟수가 이미 구한 최소 횟수보다 크거나 같다면 더 탐색할 필요가 없다.
        if cnt >= min_count:
            return
            
        # 1. 종료 조건 (Base Case)
        # 현재 위치가 종점(N-1)과 같거나 넘어섰다면 탐색을 종료한다.
        if idx >= N - 1:
            # 지금까지 충전한 횟수를 비교하여 최소값을 갱신한다. (변수 할당 필수)
            min_count = min(min_count, cnt)
            return

        # 2. 재귀 호출 (Branching)
        # 현재 정류장에서 갈 수 있는 최대 칸수(lst[idx])부터 1칸까지 역순으로 탐색한다.
        # 인자 4개 오류 수정: range(시작, 끝(포함 안 됨), 증감)
        for i in range(lst[idx], 0, -1):
            # i만큼 이동해서 다음 정류장으로 가고, 충전 횟수를 1 증가시킨다.
            backtracking(idx + i, cnt + 1)

    # 3. 탐색 시작
    # 출발점(인덱스 0)에서 시작한다.
    # 문제 조건에서 출발 정류장의 배터리 장착은 교체 횟수에 포함하지 않으므로,
    # 첫 점프 시 더해질 횟수를 상쇄하기 위해 cnt를 -1로 시작한다.
    backtracking(0, -1)
    
    print(f'#{tc} {min_count}')