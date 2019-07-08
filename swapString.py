a=list(input())
k=len(a)

for i in range(0,k,2):
    temp=a[i]
    a[i]=a[i+1]
    a[i+1]=temp
print("".join(a))
    

    
        
