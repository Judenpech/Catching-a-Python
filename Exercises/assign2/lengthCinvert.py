n=input()
if n[-1]=='m':
    inch=eval(n[0:-1])*39.37
    print("{:.03f}in".format(inch))
elif n[-1]=='n':
    mi=eval(n[0:-2])/39.37
    print("{:.03f}m".format(mi))
