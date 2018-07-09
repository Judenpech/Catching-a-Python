import math


def main():
    flag = 1
    try:
        n = input()
        if not n.isdigit() or int(n) <= 0:
            raise Exception
        flag = 0
    except:
        print("输入有误，请输入正整数")
    if flag == 0:
        sum = 0
        end = int(n) + 1
        for i in range(1, end):
            sum += math.factorial(i)
        print(sum)


main()
