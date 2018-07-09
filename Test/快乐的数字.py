def main():
    n = input()
    cnt = 0
    while n != '0':
        cnt += 1
        sum = 0
        for i in n:
            sum += int(i) * int(i)
        if sum == 1:
            print('True')
            break
        n = str(sum)
        if cnt > 100:
            print('False')
            break


main()
