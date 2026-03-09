#중복 순열
# [0,1,2] 3개의 카드가 존재(2개를 뽑는 모든 경우)

#기저조건 : 2개의 카드를 모두 뽑았을 경우
# - 시작: 0개의 카드를 고른상태부터 시작
# 다음 재귀 호출: 카드 3개 중 하나를 선택

path = []


def recur(count):
    if count ==3:
        print(path)
        return
    #한 번의 선택에서 3가지 경우의 수
    for i in range(3):
        path.append(i)  #해당 숫자를 경로에 추가
        recur(count+1)
        path.pop()      #숫자를 뽑은 적이 없도록 초기화

    # #0을 선택
    # path.append(0)
    # recur(count+1)
    # path.pop()

    # #1을 선택
    # path.append(1)
    # recur(count+1)
    # path.pop()

    # #2를 선택    
    # path.append(2)
    # recur(count+1)
    # path.pop()

recur(0)

#[심화] 경로를 전역변수 쓰지 않고 하는 방법

def recur2(count):
    if count == 2:
        return
    
    for i in range(3):
        recur2(count)
    
recur(0)