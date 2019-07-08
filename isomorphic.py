a,b=map(str,input().split())
if(len(a)!=len(b)):
    print("no")
else:
    
    
    c1=[a.count(i)for i in a]
    c2=[b.count(i) for i in b]
if(c1==c2):
    print("yes")
else:
    print("no")
        
        
