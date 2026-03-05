T = int(input())
for tc in range(1, T + 1):
    N = float(input())

    #실수를 이진수로 바꾼 결과
    binary = ''
    #자릿수 확인용 카운트
    count = 0

    #반복을 하면서 이진수로 바꾸기
    #N은 이진수로 생각하면
    #왼쪽으로 한칸씩 땡겨서 1인지 0인지 확인
    #1이 나오면 1써주고 1빼주고
    #0이 나오면 0써주고 다음 자리로
    #반복
    while N != 0 and count < 13:
        N *= 2
        if N >= 1:
            binary += '1'
            N -= 1
        else:
            binary += '0'
        count += 1

    #13자리가 다 채워지지 않았는데 N이 0이 되면
    #그건 정확한 이진수 표현이 아님
    if N != 0:
        binary = 'overflow'

    print(f"#{tc} {binary}")