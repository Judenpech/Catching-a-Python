n=input()
if n[0:3]=='RMB':
    usd=eval(n[3:])/6.78
    print("USD{:.2f}".format(usd))
elif n[0:3]=='USD':
    rmb=eval(n[3:])*6.78
    print("RMB{:.2f}".format(rmb))
