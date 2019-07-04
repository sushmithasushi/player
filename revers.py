def rev(x):
    temp=x
    an=0
    while temp!=0:
        rem=temp%10
        an=an*10+rem
        temp=temp//10
    print(an)
    
x=int(input(""))

rev(x)
