N,M=map(int, input().split())

arr = [i for i in range(1,N+1)]
#방명록 만들기
selected = [0] * len(arr)
#재귀함수 i = 현재수 path = 지금까지 선택한 수 selected = 방명록
def perm(i,path,selected):
    #
    if i == M:
        print(*path)
        return
    
    for j in range(len(arr)):
        if not selected[j]:
            path.append(arr[j])
            selected[j]=1
            
            perm(i+1, path, selected)
            
            path.pop()
            selected[j] = 0
            
perm(0,[],selected)