#N的多次方
n=input()
for i in range(0,6):
    if(i!=0):print(" ",end="")
    print(pow(eval(n),i),end="")
