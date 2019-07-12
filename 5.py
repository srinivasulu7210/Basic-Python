x=int(input("Enter a number:"))
temp=2*x-1
low=0
high=temp-1
l1=[[0 for i in range(temp)]for i in range(temp)]
for i in range(x):
    for j in range(low,high+1):
        l1[low][j]=x
    for k in range(low,high+1):
        l1[k][high]=x
    for l in range(low,high+1):
        l1[high][l]=x
    for m in range(low,high+1):
        l1[m][low]=x
    low+=1
    high-=1
    x-=1
for i in range(temp):
    for j in range(temp):
        print(l1[i][j],end=" ")
    print()
