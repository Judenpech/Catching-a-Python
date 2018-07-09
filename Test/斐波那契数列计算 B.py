def F(n):
    if n == 0 or n == 1:
        return n
    return F(n - 1) + F(n - 2)


def main():
    n = eval(input())
    sum = 0
    for i in range(0, n + 1):
        t = F(i)
        print(t, end=", ")
        sum += F(i)
    print(str(sum) + ", " + str(sum // (n + 1)))


main()
