sum,tmp=0,1
for i in range(1,11):
    tmp*=i
    sum+=tmp
print("1+2!+3!+...+10!={}".format(sum))
