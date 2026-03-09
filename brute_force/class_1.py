#도전문제 1
# 0 1 2 3 4 5 5 4 3 2 1 0
#재귀호출 사용해 구현

#현재 몇번 반복(재귀호출) 했는지 나타낼 파라미터 필요
def recur(num):
    #1. 종료조건
    if num > 5:
        return
    #2. 재귀호출
    # 종료조건에 점점 가까워지도록
    print(num, end=' ')
    recur(num+1)
    print(num, end=' ')
recur(0)    