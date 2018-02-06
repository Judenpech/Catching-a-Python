#extension.py
def getExt(fName):
    dot=fName.rfind('.')
    if dot==-1:
        return ''
    else:
        return fName[dot+1:]

def main():
    print (getExt("hello.txt"))
    print (getExt("pizza.py"))
    print (getExt("pizza.old.py"))
    print (getExt("pizza"))

main()
