
s=int(input())
l=list(input())
res=[]
ss=['a','e','i','o','u']
for i in l:
    if i not in ss:
        res.append(i)
for i in range(len(res)-1,-1,-1):
    print(res[i],end="")
