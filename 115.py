n=int(input())
l=list(map(int,input().split()[:n]))
res=[]
for i in l:
    res.append(i)
res.sort()
for i in range(n):
    print(l.index(res[i])+1,end=" ")
