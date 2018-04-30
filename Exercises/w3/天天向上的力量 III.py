n=eval(input())
a=pow(1.0+n*0.001,365)
b=pow(1.0-n*0.001,365)

print("{:.2f},{:.2f},{:.0f}".format(a,b,a//b))
