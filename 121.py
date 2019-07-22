n,m=map(int,input().split())
s=list(map(int,input().split()[:m+n]))
res=[]
for i in s:
    if s.count(i)>1:
        res.append(i)
res.sort()
print(res)
