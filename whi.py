def fun7(*a):
    i=0;s=0;
    while i<len(a):
        if a[i]%2==0:
            s+=a[i]
        i+=1
    print(s)
fun7(1,7,8,25,30,60,70)

