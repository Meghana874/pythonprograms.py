a=int(input())
b=int(input())
if a>b:
    print("INVALID INPUT")
else:
    count=0
    for i in range(a,b+1):
        if i%11==0:
            print(i,end=" ")
            count=count+1
    if(count==0):
        print("no number")