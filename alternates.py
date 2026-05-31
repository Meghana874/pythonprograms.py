a=10
b=25
c=0
count=0
sum=0
for i in range(a,b+1):
    if i%2==0:
        c=c+1
    if c%2==1:
        sum=sum+i
        count=count+i
print(sum/count)

