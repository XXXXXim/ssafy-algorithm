N, M = map(int,input().split())

arr = [i for i in range(1, N+1)]

def recur(i,path):
    if i == M:
        print(*path)
        return
    
    for num in arr:
        path.append(num)
        
        recur(i+1, path)
        path.pop()
recur(0,[])