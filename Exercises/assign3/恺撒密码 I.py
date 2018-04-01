s=input()
for i in range(len(s)):
    if s[i]>='a' and s[i]<='z':
        t=(ord(s[i])-97+3)%26+97;
        print(chr(t),end="")
    else:
        print(s[i],end="")
