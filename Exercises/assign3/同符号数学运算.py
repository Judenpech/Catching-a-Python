n=eval(input())
if n>=0:
    flag=1
else:
    flag=-1
abss=abs(n)
add=(abss+10)*flag
subs=(abss-10)*flag
if n>=0 and subs<0:
    subs=-1*subs
if n<0 and subs>0:
    subs=-1*subs
times=(abss*10)*flag
print("{:.0f} {:.0f} {:.0f} {:.0f}".format(abss,add,subs,times))
