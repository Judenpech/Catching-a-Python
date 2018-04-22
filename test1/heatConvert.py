def main():
    n = input()
    if n[-1] == 'J':
        cal = eval(n[:-1]) / 4.1858518
        print("{:.3f}cal".format(cal))
    elif n[-1] == 'l':
        joule = eval(n[:-3]) * 4.1858518
        print("{:.3f}J".format(joule))


main()
