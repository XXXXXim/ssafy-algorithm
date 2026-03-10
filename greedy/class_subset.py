#3명의 친구 부분집합
arr = ['O', 'X']
path= []
#3명의 친구: depth는 3
#O,X중 하나 선택: branch는 2개 
def recur(cnt):
    if cnt == 3:
        print(*path)
        return
    

    #O룰 선택
    path.append(arr[0])
    recur(cnt+1)
    path.pop()
    #X를 선택
    path.append(arr[1])
    recur(cnt+1)
    path.pop()
 

recur(0)
# ------------------------
#아래 코드를 좀 더 많이 활용하게 될것이오
name = ['MIN', 'CO', 'TIM']

def recur2(idx,subset):
    if idx == 3:
        print(*subset)
        return
    #포함하는 경우
    recur2(idx + 1, subset + [name[idx]])
    #안하는 경우
    recur2(idx +1, subset)
recur2(0,[])