
def recur(count):
    if count ==3:
        print(path)
        return
    #한 번의 선택에서 3가지 경우의 수
    for i in range(3):
        if i in path:
            continue


        path.append(i)  #해당 숫자를 경로에 추가
        recur(count+1)
        path.pop()      #숫자를 뽑은 적이 없도록 초기화
recur(0)

path = []
N =3
used = [0] * N 

def recur2(count):
    if count ==3:
        print(*path)
        return
    
    for i in range(3):
        if used[i]:     #이미 i를 사용한 적이 있다면
            continue

        used[i] = 1     #방문처리
        path.append(i)
        recur2(count + 1)
        path.pop()
        used[i] = 0 #방문기록 초기화