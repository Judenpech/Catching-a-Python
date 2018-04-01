n=eval(input())
for i in range(n//2+1):
    for j in range(n//2-i):
        print(" ",end="")
    for k in range(i*2+1):
        print("*",end="")
    for j in range(n//2-i):#太严格了，后面的空格也需要输出
        print(" ",end="")
    print()
