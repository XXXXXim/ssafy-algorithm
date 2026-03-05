T = int(input())

for tc in range(1, T + 1):
    # 실수 N 입력받기
    N = float(input())

    # 실수를 이진수로 바꾼 결과
    bin = ""
    # 자릿수 확인용 카운트
    cnt = 0

    # 반복을 하면서 이진수로 바꾸기
    # N은 이진수로 생각하면
    # 왼쪽으로 한칸씩 땡겨서 1인지 0인지 확인
    # 왼쪽 땡긴다 => 왼쪽시프트 => *2
    # 1이나오면 1 써주고 1빼주고 다음 자리로
    # 0이나오면 0 써주고 다음 자리로
    # 반복
    while cnt < 13 and N != 0:
        # 한칸 왼쪽으로 밀기
        N = N * 2
        # 민 횟수 +1
        cnt += 1
        # 1이 튀어나왓는지 0이 튀어나왓는지
        if N >= 1:
            bin += "1"
            N -= 1
        else:
            bin += "0"

    if cnt < 13:
        print(f"#{tc} {bin}")
    else:
        print(f"#{tc} overflow")
