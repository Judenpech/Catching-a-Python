n=input()
if n[0]=='C':
    f=eval(n[1:])*1.8+32
    print("F{:.2f}".format(f))
elif n[0]=='F':
    c=(eval(n[1:])-32)/1.8
    print("C{:.2f}".format(c))
