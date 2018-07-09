import operator


def main():
    l = [[]]
    l = eval(input())
    l.sort(key=operator.itemgetter(1))
    l.sort(key=operator.itemgetter(0), reverse=True)
    output = []
    for i in l:
        output.insert(i[1], i)
    print(output)


main()
